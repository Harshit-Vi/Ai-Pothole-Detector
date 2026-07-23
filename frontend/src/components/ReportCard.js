import React from 'react';
import './Dashboard.css';

const ReportCard = ({ report }) => {
  const getSeverityColor = (severity) => {
    const colors = {
      minor: '#FFC107',
      medium: '#FF9800',
      severe: '#F44336'
    };
    return colors[severity] || '#9E9E9E';
  };

  return (
    <div className="report-card">
      <div className="card-header">
        <h3>{report.address || 'Unknown Location'}</h3>
        <span
          className="severity-badge"
          style={{ backgroundColor: getSeverityColor(report.severity) }}
        >
          {report.severity.toUpperCase()}
        </span>
      </div>
      <div className="card-body">
        <p><strong>Location:</strong> {report.latitude.toFixed(4)}, {report.longitude.toFixed(4)}</p>
        <p><strong>Status:</strong> {report.status}</p>
        <p><strong>Reported:</strong> {new Date(report.reported_at).toLocaleDateString()}</p>
        {report.description && <p><strong>Description:</strong> {report.description}</p>}
      </div>
    </div>
  );
};

export default ReportCard;
