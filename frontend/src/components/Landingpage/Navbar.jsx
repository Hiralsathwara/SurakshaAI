import { Link } from "react-router-dom";

function Navbar() {
    return (
        <header className="landing-navbar">
            <a className="brand" href="#home">
                <span className="brand-icon">🛡️</span>
                <span>SurakshaAI</span>
            </a>

            <nav className="nav-links" aria-label="Primary navigation">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#features">Features</a>
                <Link to="/login">Sign In</Link>
                <Link to="/register" className="nav-cta">
                    Sign Up
                </Link>
            </nav>
        </header>
    );
}

export default Navbar;
