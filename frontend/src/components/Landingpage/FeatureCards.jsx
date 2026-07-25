const features = [
    {
        title: "AI Scam Detection",
        description: "Detect scam SMS, emails, and suspicious messages using machine learning models.",
    },
    {
        title: "OCR Scanner",
        description: "Extract text from screenshots and analyze suspicious payment or fraud content.",
    },
    {
        title: "Voice Assistant",
        description: "Speak naturally and receive immediate cyber safety guidance in simple language.",
    },
    {
        title: "Financial Literacy",
        description: "Learn banking safety, UPI security, OTP protection, and phishing awareness.",
    },
    {
        title: "Emergency Help",
        description: "Get instant guidance after financial fraud with trusted emergency actions.",
    },
];

function FeatureCards() {
    return (
        <section className="features-section" id="features">
            <div className="section-heading">
                <p className="section-label">Platform Features</p>
                <h2>Everything you need to stay safe online</h2>
            </div>

            <div className="feature-grid">
                {features.map((feature) => (
                    <article className="feature-card" key={feature.title}>
                        <h3>{feature.title}</h3>
                        <p>{feature.description}</p>
                    </article>
                ))}
            </div>
        </section>
    );
}

export default FeatureCards;
