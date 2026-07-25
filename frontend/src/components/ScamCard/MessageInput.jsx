
import "./MessageInput.css";
function MessageInput({ 
    message,
    setMessage,
    onAnalyze,
    loading,
    clearError }) {

    const maxCharacters = 1000;

    return (

        <div>

            <label>

                Enter suspicious message

            </label>

            <textarea
                rows="8"
                value={message}
                maxLength={maxCharacters}
                placeholder="Paste SMS, Email or WhatsApp message..."
                onChange={(e)=>{
                        setMessage(e.target.value);
                        clearError();
                        // setError("");
                    }}
            />

            <div className="message-footer">

                <span>

                    {message.length}/{maxCharacters}

                </span>

                <button
                    onClick={onAnalyze}
                    disabled={loading}
                >
                    {loading ? "Analyzing..." : "Analyze Message"}

                </button>

            </div>

        </div>

    );
}

export default MessageInput;