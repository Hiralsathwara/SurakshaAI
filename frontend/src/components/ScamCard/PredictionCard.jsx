import "./PredictionCard.css";

function PredictionCard({ result }) {

    if (!result) {
        return (
            <div className="prediction-card">
                <h2>Prediction Result</h2>
                <p>No prediction yet.</p>
            </div>
        );
    }

    const prediction = result.prediction || "Unknown";
    const confidence = result.confidence || 0;

    const riskLevel = result.risk_level || "Pending AI Analysis";
    const category = result.category || "Pending AI Analysis";

    const explanation =
        result.explanation ||
        "AI explanation will be available after the AI Explanation Engine is implemented.";

    const reasons = result.reasons || [];

    const recommendations = result.recommendations || [];

    return (

        <div className="prediction-card">

            <div className={`prediction-header ${prediction === "Scam" ? "danger" : "safe"}`}>

                <h2>
                    {prediction === "Scam"
                        ? "🚨 Scam Detected"
                        : "✅ Safe Message"}
                </h2>

            </div>

            <div className="prediction-grid">

                <div className="prediction-item">
                    <span>Prediction</span>
                    <strong>{prediction}</strong>
                </div>

                <div className="prediction-item">
                    <span>Confidence</span>
                    <strong>{confidence}%</strong>
                </div>

                <div className="prediction-item">
                    <span>Risk Level</span>
                    <strong>{riskLevel}</strong>
                </div>

                <div className="prediction-item">
                    <span>Category</span>
                    <strong>{category}</strong>
                </div>

            </div>

            <div className="confidence-section">

                <p>Confidence Score</p>

                <div className="progress">

                    <div
                        className="progress-bar"
                        style={{ width: `${confidence}%` }}
                    ></div>

                </div>

            </div>

            <div className="section">

                <h3>🤖 AI Explanation</h3>

                <p>{explanation}</p>

            </div>

            <div className="section">

                <h3>📌 Reasons</h3>

                {
                    reasons.length > 0 ? (

                        <ul>

                            {reasons.map((item, index) => (

                                <li key={index}>✔ {item}</li>

                            ))}

                        </ul>

                    ) : (

                        <p>Reasons will appear after AI analysis.</p>

                    )
                }

            </div>

            <div className="section">

                <h3>🛡 Recommended Actions</h3>

                {
                    recommendations.length > 0 ? (

                        <ul>

                            {recommendations.map((item, index) => (

                                <li key={index}>✔ {item}</li>

                            ))}

                        </ul>

                    ) : (

                        <p>Recommendations will appear after AI analysis.</p>

                    )
                }

            </div>

        </div>

    );

}

export default PredictionCard;