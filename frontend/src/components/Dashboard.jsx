import React from 'react';
import './Dashboard.css';

const Dashboard = ({ onLogout }) => {
  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>DigitalPassport</h1>
        <button onClick={onLogout} className="logout-button">
          Выйти
        </button>
      </header>
      
      <main className="dashboard-content">
        <div className="dashboard-welcome">
          <h2>Добро пожаловать в ваш цифровой паспорт!</h2>
          <p>Управляйте вашими цифровыми документами и данными в одном безопасном месте</p>
        </div>
        
        <div className="dashboard-card">
          <h3>📊 Мои документы</h3>
          <p>Здесь будут отображаться все ваши загруженные документы и сертификаты</p>
        </div>
        
        <div className="dashboard-card">
          <h3>👤 Профиль</h3>
          <p>Управление личной информацией и настройками аккаунта</p>
        </div>
        
        <div className="dashboard-card">
          <h3>📈 История</h3>
          <p>История действий и последние операции с вашими документами</p>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;