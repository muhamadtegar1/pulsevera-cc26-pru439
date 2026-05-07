import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:3001',
  timeout: 15000,
})

/**
 * Kirim data form ke backend → ML API
 * @param {Object} formData - 10 field input user
 * @returns {Promise<{risk_score, risk_label, top_risk_factors, recommendations}>}
 */
export async function predict(formData) {
  const { data } = await api.post('/api/predict', formData)
  return data
}

/**
 * Cek status backend dan ML API
 */
export async function checkHealth() {
  const { data } = await api.get('/api/health')
  return data
}
