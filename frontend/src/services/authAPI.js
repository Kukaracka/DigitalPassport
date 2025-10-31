import axios from 'axios';

const API_BASE = '/api';

// Создаем экземпляр axios с базовой конфигурацией
const api = axios.create({
  baseURL: API_BASE,
  withCredentials: true, // Для работы с cookies
});

class AuthAPI {
  // Логин
  async login(credentials) {
    try {
      console.log('Login attempt to:', API_BASE);
      const response = await api.post('/login', {
        username: credentials.username,
        password: credentials.password
      });
      console.log('Login success:', response.data);
      return response.data;
    } catch (error) {
      console.error('Login error:', error.response?.data || error.message);
      throw this.handleError(error);
    }
  }

  // Регистрация
  async register(userData) {
    try {
      console.log('Register attempt to:', API_BASE);
      const response = await api.post('/register', {
        username: userData.username,
        password: userData.password,
        email: userData.email,
        first_name: userData.firstName,
        last_name: userData.lastName,
        father_name: userData.fatherName || ''
      });
      console.log('Register success:', response.data);
      return response.data;
    } catch (error) {
      console.error('Register error:', error.response?.data || error.message);
      throw this.handleError(error);
    }
  }

  // Проверка авторизации
  async checkAuth() {
    try {
      const response = await api.get('/login_check');
      return response.data;
    } catch (error) {
      console.error('Auth check error:', error.response?.data || error.message);
      throw this.handleError(error);
    }
  }

  // Получение текущего пользователя
  async getCurrentUser() {
    try {
      const response = await api.get('/users/');
      return response.data;
    } catch (error) {
      console.error('Get user error:', error.response?.data || error.message);
      throw this.handleError(error);
    }
  }

  // Обработка ошибок
  handleError(error) {
    if (error.response) {
      // Сервер ответил с ошибкой
      const message = error.response.data?.detail || 'Произошла ошибка сервера';
      return new Error(message);
    } else if (error.request) {
      // Запрос был сделан, но ответ не получен
      return new Error('Не удалось подключиться к серверу. Проверьте подключение к интернету.');
    } else {
      // Что-то пошло не так при настройке запроса
      return new Error('Ошибка при выполнении запроса');
    }
  }
}

export default new AuthAPI();