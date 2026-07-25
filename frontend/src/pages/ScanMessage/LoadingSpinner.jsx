import "./LoadingSpinner.css";

function LoadingSpinner() {

    return (

        <div className="loading-container">

            <div className="spinner"></div>

            <h3>Analyzing Message...</h3>

            <p>Please wait while AI checks the message.</p>

        </div>

    );

}

export default LoadingSpinner;