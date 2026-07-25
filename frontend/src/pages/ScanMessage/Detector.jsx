
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Detector.css";

import MessageInput from "../../components/ScamCard/MessageInput";
import PredictionCard from "../../components/ScamCard/PredictionCard";
import LoadingSpinner from "../../components/ScamCard/LoadingSpinner";

import { detectScam } from "../../api/scamApi";



function Detector() {
    const navigate = useNavigate();

    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const [error, setError] = useState("");


    const handleAnalyze = async () => {

        if (!message.trim()) {

    setError("Please enter a message.");

    return;

}

    if (!message.trim()) return;

    try {

        setLoading(true);

        const response = await detectScam(message);

        setResult(response);

    }

    catch (err) {

    console.error(err);

    setResult(null);

    if (err.response) {

        setError("Server error. Please try again.");

    }

    else if (err.request) {

        setError("Cannot connect to SurakshaAI server.");

    }

    else {

        setError("Something went wrong.");

    }

}

    finally {

        setLoading(false);

    }

};

    return (

        <div className="detector-page">

            <div className="detector-container">
                <div className="detector-header">

                            <button
                                className="page-back-button"
                                onClick={() => navigate("/dashboard")}
                            >
                                ← Back
                            </button>

                        </div>

                <h1 className="detector-title">
                    🛡 SurakshaAI Scam Detector
                </h1>

                <p className="detector-subtitle">
                    Detect scam SMS, Email and WhatsApp messages using AI.
                </p>
                

                <MessageInput
                    message={message}
                    setMessage={setMessage}
                    onAnalyze={handleAnalyze}
                    loading={loading}
                    clearError={() => setError("")}
                />
                {error && (
                    <div className="error-box">
                        {error}
                    </div>
                )}

                {loading ? (
                    <LoadingSpinner />
                ) : (
                    result && 
                    <PredictionCard result={result} />
                )}

                <p className="ai-status">
                    Powered by SurakshaAI Machine Learning Engine
                </p>

            </div>

        </div>

    );
}

export default Detector;
