import React, { useState } from 'react';
import axios from 'axios';

const ReportPage = ({ apiBaseUrl }) => {
  const [formData, setFormData] = useState({
    latitude: '',
    longitude: '',
    severity: 'minor',
    description: '',
    image: null
  });
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleImageChange = (e) => {
    setFormData({ ...formData, image: e.target.files[0] });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const form = new FormData();
      if (formData.image) form.append('image', formData.image);
      form.append('latitude', formData.latitude);
      form.append('longitude', formData.longitude);
      form.append('severity', formData.severity);
      form.append('description', formData.description);

      const response = await axios.post(`${apiBaseUrl}/reports`, form);
      setMessage('Report submitted successfully!');
      setFormData({ latitude: '', longitude: '', severity: 'minor', description: '', image: null });
    } catch (error) {
      setMessage('Error submitting report. Please try again.');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="report-page" style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Report a Pothole</h1>
      {message && <div className={message.includes('Error') ? 'error' : 'success'}>{message}</div>}
      
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <div>
          <label>Latitude:</label>
          <input
            type="number"
            name="latitude"
            step="0.0001"
            value={formData.latitude}
            onChange={handleInputChange}
            required
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        
        <div>
          <label>Longitude:</label>
          <input
            type="number"
            name="longitude"
            step="0.0001"
            value={formData.longitude}
            onChange={handleInputChange}
            required
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        
        <div>
          <label>Severity:</label>
          <select
            name="severity"
            value={formData.severity}
            onChange={handleInputChange}
            style={{ width: '100%', padding: '0.5rem' }}
          >
            <option value="minor">Minor</option>
            <option value="medium">Medium</option>
            <option value="severe">Severe</option>
          </select>
        </div>
        
        <div>
          <label>Description:</label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            rows="4"
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        
        <div>
          <label>Image:</label>
          <input
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        
        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit Report'}
        </button>
      </form>
    </div>
  );
};

export default ReportPage;
