import axios from 'axios'
const BASE = 'http://localhost:8000'
export const generate = (url) => axios.post(`${BASE}/generate`, { url })
export const history = () => axios.get(`${BASE}/history`)
export const getQuiz = (id) => axios.get(`${BASE}/quiz/${id}`)
