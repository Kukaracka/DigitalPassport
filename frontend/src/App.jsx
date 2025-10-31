import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import { useAuth } from './hooks/useAuth';
import { clearAuthCookies, setManualLogoutFlag, clearManualLogoutFlag, isManualLogout } from './utils/cookieManager';
import './App.css';

function App() {
  const { 
    isAuthenticated, 
    user, 
    loading, 
    error, 
    login, 
    register, 
    logout 
  } = useAuth();

  const [currentView, setCurrentView] = useState('login');
  const [manualLogout, setManualLogout] = useState(isManualLogout());

  // Обработчик выхода
  const handleLogout = async () => {
    // Очищаем cookies ПЕРЕД вызовом API logout
    clearAuthCookies();
    setManualLogoutFlag();
    
    await logout();
    setManualLogout(true);
  };

  // Сбрасываем флаг manualLogout при успешной проверке auth
  useEffect(() => {
    if (isAuthenticated) {
      setManualLogout(false);
      clearManualLogoutFlag();
    }
  }, [isAuthenticated]);

  // Обработчики переключения между формами
  const handleSwitchToLogin = () => {
    setCurrentView('login');
    setManualLogout(false);
    clearManualLogoutFlag();
  };

  const handleSwitchToRegister = () => {
    setCurrentView('register');
    setManualLogout(false);
    clearManualLogoutFlag();
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Проверка авторизации...</p>
      </div>
    );
  }

  // Если пользователь вышел вручную - не показываем dashboard
  if (isAuthenticated && !manualLogout) {
    return <Dashboard user={user} onLogout={handleLogout} />;
  }

  return (
    <div className="App">
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}
      
      {currentView === 'login' ? (
        <Login 
          onSwitchToRegister={handleSwitchToRegister}
          onLogin={login}
          error={error}
        />
      ) : (
        <Register 
          onSwitchToLogin={handleSwitchToLogin}
          onRegister={register}
          error={error}
        />
      )}
    </div>
  );
}

export default App;