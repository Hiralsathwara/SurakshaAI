import api from "./axios";

export const getDashboardSummary = async () => {

    const response = await api.get(

        "/dashboard/summary"

    );

    return response.data;

};

export const getWeeklyTrend = async () => {

    const response = await api.get(

        "/dashboard/trend"

    );

    return response.data;

};

export const getScamCategories = async()=>{

    const response = await api.get(
        "/dashboard/categories"
    );

    return response.data;

};