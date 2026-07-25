import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const sendMessage = async (message) => {

    const response = await axios.post(
        `${API_URL}/chatbot/chat`,
        {
            message
        }
    );

    return response.data;

};