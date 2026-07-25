


import { useNavigate } from "react-router-dom";
import { useState, useRef, useEffect } from "react";
import "./VoiceAssistant.css";
import { analyzeVoice } from "../../api/voiceApi";

// Supported Languages List
const LANGUAGES = [
  { code: "gu", name: "ગુજરાતી (Gujarati)" },
  { code: "hi", name: "हिंदी (Hindi)" },
  { code: "en", name: "English" },
  { code: "mr", name: "मરાઠી (Marathi)" },
  { code: "ta", name: "தமிழ் (Tamil)" },
  { code: "te", name: "తెలుగు (Telugu)" },
];

function VoiceAssistant() {
  const navigate = useNavigate();
  const [selectedLanguage, setSelectedLanguage] = useState("gu"); // Default to Gujarati
  const [audio, setAudio] = useState(null);
  const [audioPreview, setAudioPreview] = useState("");
  const [recording, setRecording] = useState(false);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("Select language and record or upload your voice message.");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const setAudioFile = (file) => {
    if (audioPreview) {
      URL.revokeObjectURL(audioPreview);
    }
    setAudio(file);
    setAudioPreview(URL.createObjectURL(file));
    setStatus("Audio ready. Click Analyze Voice to continue.");
  };

  const audioBufferToWav = (buffer) => {
    const numOfChan = buffer.numberOfChannels;
    const length = buffer.length * numOfChan * 2 + 44;
    const bufferArray = new ArrayBuffer(length);
    const view = new DataView(bufferArray);
    let offset = 0;

    const writeString = (str) => {
      for (let i = 0; i < str.length; i += 1) {
        view.setUint8(offset + i, str.charCodeAt(i));
      }
      offset += str.length;
    };

    const floatTo16BitPCM = (output, offset, input) => {
      for (let i = 0; i < input.length; i += 1, offset += 2) {
        let s = Math.max(-1, Math.min(1, input[i]));
        s = s < 0 ? s * 0x8000 : s * 0x7fff;
        view.setInt16(offset, s, true);
      }
    };

    writeString("RIFF");
    view.setUint32(offset, length - 8, true);
    offset += 4;
    writeString("WAVE");
    writeString("fmt ");
    view.setUint32(offset, 16, true);
    offset += 4;
    view.setUint16(offset, 1, true);
    offset += 2;
    view.setUint16(offset, numOfChan, true);
    offset += 2;
    view.setUint32(offset, buffer.sampleRate, true);
    offset += 4;
    view.setUint32(offset, buffer.sampleRate * numOfChan * 2, true);
    offset += 4;
    view.setUint16(offset, numOfChan * 2, true);
    offset += 2;
    view.setUint16(offset, 16, true);
    offset += 2;
    writeString("data");
    view.setUint32(offset, length - offset - 4, true);
    offset += 4;

    if (numOfChan === 2) {
      floatTo16BitPCM(view, offset, buffer.getChannelData(0));
      offset += buffer.length * 2;
      floatTo16BitPCM(view, offset, buffer.getChannelData(1));
    } else {
      floatTo16BitPCM(view, offset, buffer.getChannelData(0));
    }

    return new Blob([view], { type: "audio/wav" });
  };

  const convertFileToWav = async (file) => {
    if (file.type === "audio/wav" || file.name.toLowerCase().endsWith(".wav")) {
      return file;
    }

    try {
      const arrayBuffer = await file.arrayBuffer();
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
      const wavBlob = audioBufferToWav(audioBuffer);
      audioContext.close();
      return new File([wavBlob], "voice.wav", { type: "audio/wav" });
    } catch (err) {
      console.error(err);
      throw new Error("Unsupported audio file. Please use WAV, MP3, or M4A.");
    }
  };

  useEffect(() => {
    return () => {
      if (audioPreview) {
        URL.revokeObjectURL(audioPreview);
      }
    };
  }, [audioPreview]);

  // Persistent Refs for Audio
  const mediaRecorderRef = useRef(null);
  const mediaStreamRef = useRef(null);
  const audioContextRef = useRef(null);
  const silenceTimerRef = useRef(null);
  const animationFrameRef = useRef(null);
  const audioChunksRef = useRef([]);

  // =====================================================
  // Silence Detection
  // =====================================================
  const detectSilence = (stream) => {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    audioContextRef.current = audioContext;

    const analyser = audioContext.createAnalyser();
    analyser.fftSize = 512;
    const microphone = audioContext.createMediaStreamSource(stream);
    microphone.connect(analyser);

    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);

    const SILENCE_THRESHOLD = 15;
    const SILENCE_DURATION = 5000;

    const checkAudioLevel = () => {
      analyser.getByteFrequencyData(dataArray);

      let sum = 0;
      for (let i = 0; i < bufferLength; i++) {
        sum += dataArray[i];
      }
      const averageVolume = sum / bufferLength;

      if (averageVolume > SILENCE_THRESHOLD) {
        if (silenceTimerRef.current) {
          clearTimeout(silenceTimerRef.current);
          silenceTimerRef.current = null;
        }
      } else {
        if (!silenceTimerRef.current) {
          silenceTimerRef.current = setTimeout(() => {
            console.log("Silence detected for 5s. Stopping recording...");
            stopRecording();
          }, SILENCE_DURATION);
        }
      }

      animationFrameRef.current = requestAnimationFrame(checkAudioLevel);
    };

    checkAudioLevel();
  };

  // =====================================================
  // Start Recording
  // =====================================================
  const startRecording = async () => {
    try {
      setError("");
      setAudio(null);
      setResult(null);

      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaStreamRef.current = stream;

      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = async () => {
        const rawBlob = new Blob(audioChunksRef.current, { type: mediaRecorder.mimeType });
        const rawFile = new File([rawBlob], "recording.webm", { type: mediaRecorder.mimeType });
        
        try {
          // Convert browser recording (webm/ogg) to true WAV format
          const wavFile = await convertFileToWav(rawFile);
          setAudioFile(wavFile);
        } catch (err) {
          setAudioFile(rawFile);
        }
      };

      mediaRecorder.start();
      setRecording(true);
      detectSilence(stream);
    } catch (err) {
      console.error(err);
      setError("Microphone permission denied");
    }
  };

  // =====================================================
  // Stop Recording
  // =====================================================
  const stopRecording = () => {
    if (silenceTimerRef.current) {
      clearTimeout(silenceTimerRef.current);
      silenceTimerRef.current = null;
    }
    if (animationFrameRef.current) {
      cancelAnimationFrame(animationFrameRef.current);
    }
    if (audioContextRef.current && audioContextRef.current.state !== "closed") {
      audioContextRef.current.close();
    }
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== "inactive") {
      mediaRecorderRef.current.stop();
    }
    if (mediaStreamRef.current) {
      mediaStreamRef.current.getTracks().forEach((track) => track.stop());
    }

    setRecording(false);
  };

  // =====================================================
  // Analyze Voice
  // =====================================================
  const handleAnalyze = async () => {
    if (!audio) {
      setError("Please record or upload an audio file before analyzing.");
      return;
    }

    try {
      setLoading(true);
      setResult(null);
      setError("");
      setStatus("Analyzing voice message...");

      // Send audio file + selected language code
      const response = await analyzeVoice(audio, selectedLanguage);
      setResult(response);
      setStatus("Analysis complete.");
    } catch (err) {
      console.error(err);
      setError("Voice analysis failed");
      setStatus("Analysis failed. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="voice-page">
      <div className="voice-container">
          <button
          className="page-back-button"
          onClick={() => navigate("/dashboard")}
        >
          ← Back
        </button>

        <h1>SurakshaAI Voice Assistant</h1>
        <p className="subtitle">
          Detect scam voice messages instantly in your preferred language
        </p>

        {/* Language Selection Dropdown */}
        <div className="language-selector">
          <label htmlFor="languageSelect">Select Language:</label>
          <select
            id="languageSelect"
            value={selectedLanguage}
            onChange={(e) => setSelectedLanguage(e.target.value)}
            disabled={recording || loading}
          >
            {LANGUAGES.map((lang) => (
              <option key={lang.code} value={lang.code}>
                {lang.name}
              </option>
            ))}
          </select>
        </div>

        <div className="mic-area">
          <button
            className={recording ? "mic-btn recording" : "mic-btn"}
            onClick={recording ? stopRecording : startRecording}
          >
            {recording ? "Stop" : "Record"}
          </button>

          <p>
            {recording
              ? "Listening... (Stops automatically after 5s of silence)"
              : "Record a voice message or upload an audio file."}
          </p>
        </div>

        <div className="upload-area">
          <label htmlFor="audioUpload" className="upload-label">
            Browse .mp3 or .m4a file
          </label>
          <input
            id="audioUpload"
            type="file"
            accept="audio/mp3,audio/mpeg,audio/mp4,audio/x-m4a,audio/m4a,audio/wav"
            onChange={async (event) => {
              const file = event.target.files?.[0];
              if (file) {
                setError("");
                setResult(null);
                try {
                  const wavFile = await convertFileToWav(file);
                  setAudioFile(wavFile);
                } catch (err) {
                  console.error(err);
                  setError(err.message || "Unable to convert audio file.");
                  setStatus("Select language and record or upload your voice message.");
                }
              }
            }}
          />
        </div>

        {audioPreview && (
          <div className="preview-area">
            <p>Selected audio:</p>
            <audio controls src={audioPreview} />
          </div>
        )}

        {audio && (
          <button className="analyze-btn" onClick={handleAnalyze}>
            Analyze Voice
          </button>
        )}

        <div className="status-label">{status}</div>

        {loading && <div className="loader">Processing Voice...</div>}

        {error && <p className="error">{error}</p>}

        {result && (
          <div className="result-card">
            <h2>Result</h2>
            <p>
              <b>Language:</b>{" "}
              {LANGUAGES.find((lang) => lang.code === result.language)?.name || selectedLanguage}
            </p>
            <p>
              <b>Text:</b> {result.text}
            </p>
            <p>
              <b>Status:</b> {result.prediction}
            </p>
            <p>
              <b>Confidence:</b> {result.confidence}%
            </p>
            <p>
              <b>Advice:</b> {result.response}
            </p>

            {result.audio && <audio controls src={result.audio} />}
          </div>
        )}
      </div>
    </div>
  );
}

export default VoiceAssistant;  
