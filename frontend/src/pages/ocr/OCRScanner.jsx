


import { useState } from "react";
import { useNavigate } from "react-router-dom";

import "./OCRScanner.css";
import { scanOCR } from "../../api/ocrApi";


function OCRScanner() {
   const navigate = useNavigate();
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const allowedTypes = ["image/png", "image/jpeg", "image/jpg"];

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setError("");

    if (!allowedTypes.includes(file.type)) {
      setSelectedFile(null);
      setPreview(null);
      setError("Only PNG, JPG and JPEG images are allowed.");
      return;
    }

    if (file.size > 5 * 1024 * 1024) {
      setSelectedFile(null);
      setPreview(null);
      setError("Image size must be less than 5 MB.");
      return;
    }

    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));
  };

  const removeImage = () => {
    setSelectedFile(null);
    setPreview(null);
    setError("");
    setResult(null);
  };

  const handleScan = async () => {
    if (!selectedFile) return;

    try {
      setLoading(true);
      setResult(null);
      setError("");

      const response = await scanOCR(selectedFile);
      setResult(response);
    } catch (err) {
      console.error(err);
      setError(
        err.response?.data?.detail || "Failed to scan screenshot."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ocr-page">
        
      <div className="ocr-card">
        
        {/* Header */}
            <div className="ocr-header">

              <button
                className="page-back-button"
                onClick={() => navigate("/dashboard")}
              >
                ← Back
              </button>


              <h2>
                🛡 SurakshaAI Protected Scanner
              </h2>


              <p className="ocr-subtitle">
                Upload a UPI Screenshot for Scam Detection
              </p>

            </div>

        {/* Upload Box Container */}
        <label className={`upload-box ${preview ? "has-preview" : ""}`}>
          {preview ? (
            <img src={preview} alt="Preview" className="preview-image" />
          ) : (
            <div className="upload-placeholder">
              <span className="upload-icon">📷</span>
              
              <p className="upload-title">Click to Upload Screenshot</p>
              <span className="upload-hint">PNG, JPG, JPEG (Max 5 MB)</span>
            </div>
          )}

          <input
            type="file"
            accept="image/png, image/jpeg, image/jpg"
            hidden
            onChange={handleImageChange}
          />
        </label>

        {/* Error Alert */}
        {error && <p className="error-text">{error}</p>}

        {/* Action Buttons */}
        <div className="button-group">
          <label className="btn choose-btn">
            {preview ? "Change Image" : "Choose Image"}
            <input
              type="file"
              accept="image/png, image/jpeg, image/jpg"
              hidden
              onChange={handleImageChange}
            />
          </label>

          {preview && (
            <button className="btn remove-btn" onClick={removeImage}>
              Remove
            </button>
          )}

          <button
            className="btn scan-btn"
            disabled={!selectedFile || loading}
            onClick={handleScan}
          >
            {loading ? "Scanning..." : "Scan Screenshot"}
          </button>
        </div>

        {/* Loader */}
        {loading && (
          <div className="loading-container">
            <div className="loader"></div>
            <p>Scanning Screenshot...</p>
          </div>
        )}

        {/* OCR Result Output Box */}
        {result && (
          <div className="result-box">
            <h3>OCR Response</h3>
            <pre>{JSON.stringify(result, null, 2)}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default OCRScanner;
