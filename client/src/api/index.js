import axios from 'axios';

const API_URL = 'http://localhost:5000';

export function authenticate(userData) {
  return axios.post(`${API_URL}/login`, userData).then();
}

export function register(userData) {
  return axios.post(`${API_URL}/register`, userData);
}
