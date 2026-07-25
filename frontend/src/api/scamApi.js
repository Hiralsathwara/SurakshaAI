import api from "./axios";

export const detectScam = async (message) => {
    const response = await api.post("/detect", {
        message
    });

    return response.data;
};