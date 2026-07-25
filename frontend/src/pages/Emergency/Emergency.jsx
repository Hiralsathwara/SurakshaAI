
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getEmergencyChecklist, getBankContacts, submitEmergencyReport } from "../../api/emergencyApi";
import "./Emergency.css";

function Emergency() {
    const navigate = useNavigate();
    const [checklist, setChecklist] = useState([]);
    const [banks, setBanks] = useState([]);
    const [form, setForm] = useState({
        name: "",
        phone: "",
        bank: "",
        amount: "",
        transaction_id: "",
        incident_date: "",
        description: ""
    });
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");
    const [error, setError] = useState("");
    const [response, setResponse] = useState(null);
    const [showToast, setShowToast] = useState(false);
    const [showFreezePopup, setShowFreezePopup] = useState(false);
    const [showBlockUpiPopup, setShowBlockUpiPopup] = useState(false);

    useEffect(() => {
        const loadData = async () => {
            try {
                const checklistData = await getEmergencyChecklist();
                const bankData = await getBankContacts();
                setChecklist(checklistData.steps || []);
                setBanks(bankData || []);
            } catch (err) {
                console.error(err);
            }
        };

        loadData();
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (loading) {
            return;
        }

        setError("");
        setMessage("");
        setResponse(null);
        setShowToast(false);
        setLoading(true);

        try {
            const payload = {
                ...form,
                amount: parseFloat(form.amount)
            };

            const result = await submitEmergencyReport(payload);
            setMessage("Emergency report submitted successfully.");
            setResponse(result);
            setShowToast(true);
            setForm({
                name: "",
                phone: "",
                bank: "",
                amount: "",
                transaction_id: "",
                incident_date: "",
                description: ""
            });

            window.setTimeout(() => {
                setShowToast(false);
            }, 3500);
        } catch (err) {
            console.error(err);
            const responseMessage = err?.response?.data?.detail || err?.message || "Unable to submit report right now. Please try again.";
            setError(responseMessage);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="emergency-page">
            <div className="emergency-container">
                <div className="emergency-hero">

                        <button
                            className="page-back-button"
                            onClick={() => navigate("/dashboard")}
                        >
                            ← Back
                        </button>


                        <p className="eyebrow">
                            • Emergency Help
                        </p>


                        <h1>
                            Immediate help when money is already lost
                        </h1>


                        <p>
                            This fast workflow helps users freeze accounts, call the bank,
                            reach cybercrime support, and report the fraud quickly.
                        </p>

                    </div>

                <div className="emergency-grid">
                    <section className="card">
                        <h2>What to do now</h2>
                        <ul>
                            {checklist.map((step, index) => (
                                <li key={index}>{step}</li>
                            ))}
                        </ul>
                    </section>

                    <section className="card">
                        <h2>Bank helpline numbers</h2>
                        <div className="bank-list">
                            {banks.map((bank) => (
                                <div key={bank.bank} className="bank-item">
                                    <strong>{bank.bank}</strong>
                                    <a href={`tel:${bank.number}`}>{bank.number}</a>
                                </div>
                            ))}
                        </div>
                    </section>
                </div>

                <section className="card immediate-actions-card">
                    <h2>Immediate Actions</h2>
                    <div className="action-buttons-grid">
                        <button className="action-button" onClick={() => setShowFreezePopup(true)}>
                            Freeze Bank
                        </button>

                        <button className="action-button" onClick={() => setShowBlockUpiPopup(true)}>
                            Block UPI
                        </button>

                        <button className="action-button" onClick={() => (window.location.href = "tel:1930")}>
                            Call 1930
                        </button>

                        <button className="action-button" onClick={() => window.open("https://cybercrime.gov.in", "_blank")}>
                            Report Fraud
                        </button>
                    </div>
                </section>

                <section className="card form-card">
                    <h2>Submit fraud report</h2>
                    <form onSubmit={handleSubmit}>
                        <fieldset disabled={loading} className="form-fieldset">
                            <div className="form-grid">
                                <input name="name" value={form.name} onChange={handleChange} placeholder="Your name" required />
                                <input name="phone" value={form.phone} onChange={handleChange} placeholder="Phone number" required />
                                <input name="bank" value={form.bank} onChange={handleChange} placeholder="Bank name" required />
                                <input name="amount" type="number" value={form.amount} onChange={handleChange} placeholder="Lost amount" required />
                                <input name="transaction_id" value={form.transaction_id} onChange={handleChange} placeholder="Transaction ID" required />
                                <input name="incident_date" value={form.incident_date} onChange={handleChange} type="date" required />
                            </div>
                            <textarea
                                name="description"
                                value={form.description}
                                onChange={handleChange}
                                placeholder="Describe what happened"
                                rows="4"
                                required
                            />
                        </fieldset>
                        <button type="submit" disabled={loading}>
                            {loading ? "Submitting..." : "Submit emergency report"}
                        </button>
                    </form>
                    {showToast && (
                        <div className="toast-card">
                            <p>Report submitted successfully.</p>
                        </div>
                    )}
                    {message && <p className="success-msg">{message}</p>}
                    {response && (
                        <div className="response-card">
                            <p>
                                Report ID: <strong>{response.id}</strong>
                            </p>
                            <p>
                                Submitted at: <strong>{new Date(response.created_at).toLocaleString()}</strong>
                            </p>
                        </div>
                    )}
                    {error && <p className="error-msg">{error}</p>}
                </section>
            </div>

            {showFreezePopup && (
                <div className="popup-overlay" onClick={() => setShowFreezePopup(false)}>
                    <div className="popup-card" onClick={(e) => e.stopPropagation()}>
                        <h3>Call your bank immediately and request</h3>
                        <ul>
                            <li>• Freeze account</li>
                            <li>• Freeze debit card</li>
                            <li>• Stop pending transactions</li>
                        </ul>
                        <button onClick={() => setShowFreezePopup(false)}>Close</button>
                    </div>
                </div>
            )}

            {showBlockUpiPopup && (
                <div className="popup-overlay" onClick={() => setShowBlockUpiPopup(false)}>
                    <div className="popup-card" onClick={(e) => e.stopPropagation()}>
                        <h3>Open your UPI app</h3>
                        <p>Profile</p>
                        <p>Manage UPI</p>
                        <p>Block UPI</p>
                        <p>or contact your bank.</p>
                        <div className="popup-actions">
                            <button
                                className="action-button"
                                onClick={() => {
                                    window.location.href = "upi://pay";
                                }}
                            >
                                Open UPI App
                            </button>
                            <button onClick={() => setShowBlockUpiPopup(false)}>Close</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default Emergency;

