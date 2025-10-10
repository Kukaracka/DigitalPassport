import React, { useState } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  const [currentView, setCurrentView] = useState('login');
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogin = async (loginData) => {
    console.log('Login attempt:', loginData);
    setIsAuthenticated(true);
  };

  const handleRegister = async (registerData) => {
    console.log('Register attempt:', registerData);
    alert('Регистрация успешна! Теперь войдите в систему.');
    setCurrentView('login');
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setCurrentView('login');
    localStorage.removeItem('token');
  };

  if (isAuthenticated) {
    return <Dashboard onLogout={handleLogout} />;
  }

  return (
    <div className="App">
      {currentView === 'login' ? (
        <Login 
          onSwitchToRegister={() => setCurrentView('register')}
          onLogin={handleLogin}
        />
      ) : (
        <Register 
          onSwitchToLogin={() => setCurrentView('login')}
          onRegister={handleRegister}
        />
      )}
    </div>
  );
}

export default App;