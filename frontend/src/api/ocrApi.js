import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const scanOCR = async (imageFile) => {
    const formData = new FormData();
    formData.append("file", imageFile);

    const response = await axios.post(
        `${API_URL}/ocr/scan`,
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};