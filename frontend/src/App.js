import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import HomePage from './pages/HomePage';
import ReportPage from './pages/ReportPage';
import AnalyticsPage from './pages/AnalyticsPage';
import './App.css';

function App() {
  const [apiBaseUrl] = useState(process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api');

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/dashboard" element={<Dashboard apiBaseUrl={apiBaseUrl} />} />
          <Route path="/report" element={<ReportPage apiBaseUrl={apiBaseUrl} />} />
          <Route path="/analytics" element={<AnalyticsPage apiBaseUrl={apiBaseUrl} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
