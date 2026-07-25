import { useNavigate } from "react-router-dom";

function HeroSection() {
    const navigate = useNavigate();

    return (
        <section className="hero-section" id="home">
            <div className="hero-copy">
                <div className="hero-badge">AI Powered Cyber Fraud Protection</div>
                <h1>SurakshaAI</h1>
                <p className="hero-tagline">
                    AI Powered Cyber Fraud Detection & Digital Safety Platform
                </p>
                <p className="hero-description">
                    SurakshaAI helps users identify online scams, detect fraudulent messages,
                    scan suspicious UPI screenshots, learn cyber safety, and receive emergency
                    assistance after financial fraud. Our mission is to make digital transactions
                    safer through AI.
                </p>

                <div className="feature-badges" aria-label="Key features">
                    <span>AI Scam Detection</span>
                    <span>OCR Scanner</span>
                    <span>Voice Assistant</span>
                    <span>Financial Literacy</span>
                    <span>Emergency Help</span>
                </div>

                <div className="hero-actions">
                    <button className="btn btn-primary" onClick={() => navigate("/login")}>
                        Sign In
                    </button>
                    <button className="btn btn-secondary" onClick={() => navigate("/register")}>
                        Create Account
                    </button>
                </div>
            </div>

            <div className="hero-visual" aria-hidden="true">
                <div className="glow-ring" />
                <svg viewBox="0 0 620 540" role="img" aria-label="Cyber security illustration">
                    <rect x="120" y="90" width="360" height="330" rx="34" fill="#11213D" />
                    <rect x="170" y="140" width="260" height="220" rx="24" fill="#1E293B" stroke="#334155" strokeWidth="2" />
                    <rect x="220" y="190" width="150" height="100" rx="24" fill="#0F172A" />
                    <rect x="250" y="115" width="90" height="45" rx="12" fill="#2563EB" />
                    <rect x="90" y="260" width="90" height="105" rx="20" fill="#06B6D4" />
                    <rect x="430" y="260" width="95" height="95" rx="20" fill="#10B981" />
                    <path d="M320 115L360 75L400 115" fill="none" stroke="#06B6D4" strokeWidth="10" strokeLinecap="round" />
                    <path d="M220 330L185 365L145 330" fill="none" stroke="#10B981" strokeWidth="10" strokeLinecap="round" />
                    <path d="M370 330L405 365L445 330" fill="none" stroke="#F59E0B" strokeWidth="10" strokeLinecap="round" />
                    <circle cx="300" cy="240" r="55" fill="#2563EB" opacity="0.92" />
                    <path d="M300 190L300 240L340 255" stroke="#F8FAFC" strokeWidth="12" strokeLinecap="round" strokeLinejoin="round" />
                    <circle cx="300" cy="240" r="24" fill="#F8FAFC" />
                    <rect x="175" y="360" width="250" height="28" rx="14" fill="#334155" />
                    <rect x="195" y="398" width="210" height="18" rx="9" fill="#1E293B" />
                    <path d="M250 138L265 118L300 130L315 118L330 138" fill="none" stroke="#F8FAFC" strokeWidth="7" strokeLinecap="round" />
                    <circle cx="470" cy="140" r="25" fill="#2563EB" opacity="0.35" />
                    <circle cx="150" cy="180" r="20" fill="#10B981" opacity="0.35" />
                </svg>
            </div>
        </section>
    );
}

export default HeroSection;
