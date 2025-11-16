import axios from 'axios'
const BASE = 'https://deepklarity-ai-quiz-1.onrender.com'
export const generate = (url) => axios.post(`${BASE}/generate`, { url })
export const history = () => axios.get(`${BASE}/history`)
export const getQuiz = (id) => axios.get(`${BASE}/quiz/${id}`)
