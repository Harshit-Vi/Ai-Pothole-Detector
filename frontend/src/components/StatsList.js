import React from 'react';
import './Dashboard.css';

const StatsList = ({ stats }) => {
  return (
    <div className="stats-list">
      <div className="stat-box">
        <h3>Total Reports</h3>
        <p className="stat-value">{stats.total_reports || 0}</p>
      </div>
      <div className="stat-box">
        <h3>Total Detections</h3>
        <p className="stat-value">{stats.total_detections || 0}</p>
      </div>
      <div className="stat-box">
        <h3>Minor Issues</h3>
        <p className="stat-value" style={{ color: '#FFC107' }}>
          {stats.by_severity?.minor || 0}
        </p>
      </div>
      <div className="stat-box">
        <h3>Medium Issues</h3>
        <p className="stat-value" style={{ color: '#FF9800' }}>
          {stats.by_severity?.medium || 0}
        </p>
      </div>
      <div className="stat-box">
        <h3>Severe Issues</h3>
        <p className="stat-value" style={{ color: '#F44336' }}>
          {stats.by_severity?.severe || 0}
        </p>
      </div>
    </div>
  );
};

export default StatsList;
