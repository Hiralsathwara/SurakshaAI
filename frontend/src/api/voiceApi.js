

// src/api/voiceApi.js
export const analyzeVoice = async (audioFile, language = "gu") => {
  const formData = new FormData();
  formData.append("file", audioFile);
  formData.append("language", language); // Pass language code (e.g. 'gu', 'hi', 'en')

  const response = await fetch("http://127.0.0.1:8000/voice/analyze", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to analyze voice");
  }

  return await response.json();
};