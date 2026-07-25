import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerUser } from "../../api/authApi";
import "./Register.css";

function Register() {
  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone: "",
    password: "",
    language: "English",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await registerUser(formData);
      alert("Registration successful! Please login.");
      navigate("/", { replace: true });
    } catch (error) {
      alert(error.response?.data?.detail || "Registration failed");
    }
  };

  return (
    <div className="register-container">
      <div className="register-card">
        <h1 className="logo">SurakshaAI</h1>
        <h3 className="title">Create Account</h3>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="full_name"
            placeholder="Full Name"
            value={formData.full_name}
            onChange={handleChange}
            className="input-field"
          />

          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            className="input-field"
          />

          <input
            type="text"
            name="phone"
            placeholder="Phone"
            value={formData.phone}
            onChange={handleChange}
            className="input-field"
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            className="input-field"
          />

          <select
            name="language"
            value={formData.language}
            onChange={handleChange}
            className="input-field"
          >
            <option>English</option>
            <option>Hindi</option>
            <option>Gujarati</option>
          </select>

          <button type="submit" className="register-btn">
            Create Account
          </button>

          <button
            type="button"
            className="home-btn"
            onClick={() => navigate("/")}
          >
            Home
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;
