import axios from "axios";

export const sendImage = async function sendImage(image) {
    try {
        const response = await axios.post("/api/data/sendimage", image, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }});
        return response.data
    } catch (error) {
        console.error("Unseen error while registering:", error);
        return false
    }
}