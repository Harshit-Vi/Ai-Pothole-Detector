import React from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div className="home-page">
      <nav className="navbar">
        <h1 className="logo">🛣️ AI Pothole Detector</h1>
        <div className="nav-links">
          <button onClick={() => navigate('/dashboard')}>Dashboard</button>
          <button onClick={() => navigate('/report')}>Report</button>
          <button onClick={() => navigate('/analytics')}>Analytics</button>
        </div>
      </nav>

      <section className="hero">
        <div className="hero-content">
          <h1>Smart Road Damage Detection</h1>
          <p>Real-time pothole detection powered by AI</p>
          <button className="cta-button" onClick={() => navigate('/dashboard')}>
            View Dashboard
          </button>
        </div>
      </section>

      <section className="features">
        <div className="feature-grid">
          <div className="feature-card">
            <h3>🎯 Real-time Detection</h3>
            <p>Detect potholes instantly from images and videos</p>
          </div>
          <div className="feature-card">
            <h3>📍 GPS Tagging</h3>
            <p>Automatic location identification and mapping</p>
          </div>
          <div className="feature-card">
            <h3>⚠️ Severity Classification</h3>
            <p>Classify road damage into minor, medium, or severe</p>
          </div>
          <div className="feature-card">
            <h3>🚨 Auto-Reporting</h3>
            <p>Automatic SMS/Email alerts to municipalities</p>
          </div>
          <div className="feature-card">
            <h3>📊 Analytics Dashboard</h3>
            <p>Comprehensive statistics and insights</p>
          </div>
          <div className="feature-card">
            <h3>📱 Mobile Support</h3>
            <p>Report potholes on the go from your phone</p>
          </div>
        </div>
      </section>

      <footer className="footer">
        <p>&copy; 2024 AI Pothole Detector. Built for safer roads.</p>
      </footer>
    </div>
  );
};

export default HomePage;
