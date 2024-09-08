import axios from "axios";


export const checkLogin = async function checkLogin(emailInput, passwordInput) {
    try {
        const response = await axios.post(`/api/user/login`, {
            username: emailInput,
            password: passwordInput,
        });
        return response;
    } catch (error) {
        console.error('Login error:', error);
        throw error;
    }
};

export const signupUser = async function signupUser(first, name, email, password, birthday) {
    try {
        const response = await axios.post(`/api/user/signup`, {
            email: email,
            password: password,
            birthday: birthday,
            first: first,
            name: name,
        });
        return response;
    } catch (error) {
        console.error('Sign up error:', error);
        throw error;
    }
};