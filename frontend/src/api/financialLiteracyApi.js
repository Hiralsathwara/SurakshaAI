import api from "./axios";

export const getFinancialLiteracyCategories = async () => {
    const response = await api.get("/financial-literacy/categories");
    return response.data;
};

export const getFinancialLiteracyTopic = async (topicId) => {
    const response = await api.get(`/financial-literacy/topic/${topicId}`);
    return response.data;
};
