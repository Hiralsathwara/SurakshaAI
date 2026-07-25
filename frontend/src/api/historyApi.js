import api from "./axios";

export const getHistory = async (
    search = "",
    prediction = "All",
    page = 1,
    limit = 10
) => {

    const response = await api.get("/history", {
        params: {
            search,
            prediction,
            page,
            limit
        }
    });

    return response.data;

};

export const deleteHistory = async (historyId) => {

    const response = await api.delete(`/history/${historyId}`);

    return response.data;

};