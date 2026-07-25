import api from "./axios";

export const getEmergencyChecklist = async () => {
    const response = await api.get("/emergency/checklist");
    return response.data;
};

export const getBankContacts = async () => {
    const response = await api.get("/emergency/banks");
    return response.data;
};

export const submitEmergencyReport = async (payload) => {
    const response = await api.post("/emergency/report", payload);
    return response.data;
};
