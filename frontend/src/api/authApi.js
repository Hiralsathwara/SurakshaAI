import api from "./axios";

export const registerUser = (data) =>
    api.post("/auth/register", data);

export const loginUser = (data) => {
    const params = new URLSearchParams();
    params.append("username", data.email);
    params.append("password", data.password);

    return api.post("/auth/login", params, {
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
    }).then((response) => response.data);
};

export const getProfile = (token) =>
    api.get("/auth/profile", {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    }).then((response) => response.data);