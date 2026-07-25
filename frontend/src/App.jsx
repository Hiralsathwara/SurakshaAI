import { Routes, Route } from "react-router-dom";
import "./components/Navigation/BackToDashboard.css";

import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import Dashboard from "./pages/Dashboard/Dashboard";
import NotFound from "./pages/NotFound";
import Detector from "./pages/ScanMessage/Detector";
import History from "./pages/History/History";
import OCRScanner from "./pages/ocr/OCRScanner";
import VoiceAssistant from "./pages/VoiceAssistant/VoiceAssistant";
import ChatAssistant from "./pages/ChatAssistant/ChatAssistant";
import Emergency from "./pages/Emergency/Emergency";
import FinancialLiteracy from "./pages/FinancialLiteracy/FinancialLiteracy";
import Home from "./pages/Home/LandingPage"

function App() {
    return (
        <Routes>
            <Route
                path="/"
                element={<Home />}
            />

            <Route
                path="/login"
                element={<Login />}
            />

            <Route
                path="/register"
                element={<Register />}
            />

            <Route
                path="/dashboard"
                element={<Dashboard />}
            />
            <Route 
                path="/scan-message" 
                element={<Detector />} 
             />
             <Route
                path="/history"
                element={<History />}
            />
            {/* if we are using protected route */}
                        {/* <Route
                path="/history"
                element={
                    <ProtectedRoute>
                        <History />
                    </ProtectedRoute>
                }
            /> */}
           
             <Route
                        path="/ocr"
                        element={<OCRScanner />}
            />
                
            <Route
                path="*"
                element={<NotFound />}
            />
            <Route
            path="/voice"
            element={ <VoiceAssistant/> }
            />

            <Route 
                path="/chat-assistant" 
                element={<ChatAssistant />} 
            />

            <Route
                path="/emergency"
                element={<Emergency />}
            />

            <Route
                path="/financial-literacy"
                element={<FinancialLiteracy />}
            />

        </Routes>
    );
}

export default App;
