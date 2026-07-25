import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
    getFinancialLiteracyCategories,
    getFinancialLiteracyTopic,
} from "../../api/financialLiteracyApi";
import "./FinancialLiteracy.css";

function FinancialLiteracy() {
    const navigate = useNavigate();
    const [categories, setCategories] = useState([]);
    const [selectedTopicId, setSelectedTopicId] = useState(1);
    const [topic, setTopic] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadCategories = async () => {
            try {
                const data = await getFinancialLiteracyCategories();
                setCategories(data);
            } catch (error) {
                console.error(error);
            }
        };

        loadCategories();
    }, []);

    useEffect(() => {
        const loadTopic = async () => {
            try {
                setLoading(true);
                const data = await getFinancialLiteracyTopic(selectedTopicId);
                setTopic(data);
            } catch (error) {
                console.error(error);
            } finally {
                setLoading(false);
            }
        };

        loadTopic();
    }, [selectedTopicId]);

    return (
        <div className="financial-literacy-page">
            <div className="financial-literacy-shell">
                <header className="financial-hero">
                    <div>
                        <p className="eyebrow">🛡️ Financial Literacy</p>
                        <h1>Learn how to stay safe from online financial fraud.</h1>
                        <p>
                            This page is designed to educate and raise awareness with simple, practical
                            answers about banking safety, digital payments, phishing, and scam prevention.
                        </p>
                    </div>
                    <button className="page-back-button" onClick={() => navigate("/dashboard")}>← Back to Dashboard</button>
                </header>

                <section className="card categories-card">
                    <h2>Choose a topic</h2>
                    <div className="category-grid">
                        {categories.map((category) => (
                            <button
                                key={category.id}
                                className={`category-card ${selectedTopicId === category.id ? "active" : ""}`}
                                onClick={() => setSelectedTopicId(category.id)}
                            >
                                <span className="category-icon">{category.icon}</span>
                                <span>{category.title}</span>
                            </button>
                        ))}
                    </div>
                </section>

                <section className="card content-card">
                    {loading ? (
                        <p>Loading awareness content...</p>
                    ) : topic ? (
                        <>
                            <h2>{topic.title}</h2>
                            <div className="faq-list">
                                {topic.faqs.map((faq, index) => (
                                    <article key={`${faq.question}-${index}`} className="faq-item">
                                        <h3>❓ {faq.question}</h3>
                                        <p>{faq.answer}</p>
                                    </article>
                                ))}
                            </div>
                        </>
                    ) : (
                        <p>No content available for this topic yet.</p>
                    )}
                </section>
            </div>
        </div>
    );
}

export default FinancialLiteracy;
