import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MapView from './MapView';
import ReportCard from './ReportCard';
import StatsList from './StatsList';
import FilterPanel from './FilterPanel';
import './Dashboard.css';

const Dashboard = ({ apiBaseUrl }) => {
  const [reports, setReports] = useState([]);
  const [stats, setStats] = useState({});
  const [filters, setFilters] = useState({ severity: 'all', status: 'all' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchReports();
    fetchStats();
  }, [filters]);

  const fetchReports = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${apiBaseUrl}/reports`, { params: filters });
      setReports(response.data.reports || []);
      setError(null);
    } catch (err) {
      setError('Failed to fetch reports');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchStats = async () => {
    try {
      const response = await axios.get(`${apiBaseUrl}/dashboard/stats`);
      setStats(response.data);
    } catch (err) {
      console.error('Failed to fetch stats:', err);
    }
  };

  return (
    <div className="dashboard">
      <h1>AI Pothole Detector Dashboard</h1>
      
      {error && <div className="error">{error}</div>}
      
      <StatsList stats={stats} />
      <FilterPanel filters={filters} setFilters={setFilters} />
      
      <div className="dashboard-content">
        <MapView reports={reports} />
        <div className="reports-list">
          {loading ? (
            <div className="loading"><div className="spinner"></div></div>
          ) : reports.length > 0 ? (
            reports.map(report => (
              <ReportCard key={report.id} report={report} />
            ))
          ) : (
            <p>No reports found</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
