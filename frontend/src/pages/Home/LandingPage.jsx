import Navbar from "../../components/Landingpage/Navbar";
import HeroSection from "../../components/Landingpage/HeroSection";
import FeatureCards from "../../components/Landingpage/FeatureCards";
import AboutSection from "../../components/Landingpage/AboutSection";
import Footer from "../../components/Landingpage/Footer";
import "./LandingPage.css";

function LandingPage() {
    return (
        <div className="landing-page">
            <Navbar />
            <main>
                <HeroSection />
                <FeatureCards />
                <AboutSection />
            </main>
            <Footer />
        </div>
    );
}

export default LandingPage;
