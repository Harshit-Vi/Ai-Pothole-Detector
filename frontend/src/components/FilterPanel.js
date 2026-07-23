import React, { useState } from 'react';
import './Dashboard.css';

const FilterPanel = ({ filters, setFilters }) => {
  const handleSeverityChange = (e) => {
    setFilters({ ...filters, severity: e.target.value });
  };

  const handleStatusChange = (e) => {
    setFilters({ ...filters, status: e.target.value });
  };

  return (
    <div className="filter-panel">
      <div className="filter-group">
        <label>Severity:</label>
        <select value={filters.severity} onChange={handleSeverityChange}>
          <option value="all">All</option>
          <option value="minor">Minor</option>
          <option value="medium">Medium</option>
          <option value="severe">Severe</option>
        </select>
      </div>
      <div className="filter-group">
        <label>Status:</label>
        <select value={filters.status} onChange={handleStatusChange}>
          <option value="all">All</option>
          <option value="reported">Reported</option>
          <option value="acknowledged">Acknowledged</option>
          <option value="resolved">Resolved</option>
        </select>
      </div>
    </div>
  );
};

export default FilterPanel;
