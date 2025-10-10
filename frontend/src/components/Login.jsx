import React, { useState } from 'react';
import './Auth.css';

const Login = ({ onSwitchToRegister, onLogin }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onLogin(formData);
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="auth-content">
          <h2>Вход в DigitalPassport</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                placeholder="Введите ваш email"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="password">Пароль</label>
              <input
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
                placeholder="Введите ваш пароль"
              />
            </div>

            <button type="submit" className="auth-button">
              Войти
            </button>
          </form>

          <div className="auth-switch">
            <p>Нет аккаунта? 
              <span className="switch-link" onClick={onSwitchToRegister}>
                Зарегистрироваться
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;