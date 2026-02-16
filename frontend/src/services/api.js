import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const API_BASE = `${API_URL}/api`

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Libros API
export const getLibros = async () => {
  const response = await api.get('/libros')
  return response.data
}

export const getLibro = async (id) => {
  const response = await api.get(`/libros/${id}`)
  return response.data
}

export const createLibro = async (libro) => {
  const response = await api.post('/libros', libro)
  return response.data
}

export const updateLibro = async (id, libro) => {
  const response = await api.put(`/libros/${id}`, libro)
  return response.data
}

export const deleteLibro = async (id) => {
  const response = await api.delete(`/libros/${id}`)
  return response.data
}

export const ping = async () => {
  const response = await api.get('/ping')
  return response.data
}

export default api
