import React, { useState } from 'react';
import { View, TextInput, TouchableOpacity, Text, StyleSheet, ScrollView, Alert } from 'react-native';
import axios from 'axios';

const ReportScreen = () => {
  const [formData, setFormData] = useState({
    latitude: '',
    longitude: '',
    severity: 'minor',
    description: '',
  });
  const [loading, setLoading] = useState(false);
  const apiBaseUrl = process.env.REACT_NATIVE_API_BASE_URL || 'http://localhost:5000/api';

  const handleSubmit = async () => {
    if (!formData.latitude || !formData.longitude) {
      Alert.alert('Error', 'Please enter latitude and longitude');
      return;
    }

    setLoading(true);
    try {
      await axios.post(`${apiBaseUrl}/reports`, formData);
      Alert.alert('Success', 'Report submitted successfully');
      setFormData({ latitude: '', longitude: '', severity: 'minor', description: '' });
    } catch (error) {
      Alert.alert('Error', 'Failed to submit report');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Report a Pothole</Text>

      <Text style={styles.label}>Latitude</Text>
      <TextInput
        style={styles.input}
        placeholder="28.7041"
        value={formData.latitude}
        onChangeText={(value) => setFormData({ ...formData, latitude: value })}
        keyboardType="decimal-pad"
      />

      <Text style={styles.label}>Longitude</Text>
      <TextInput
        style={styles.input}
        placeholder="77.1025"
        value={formData.longitude}
        onChangeText={(value) => setFormData({ ...formData, longitude: value })}
        keyboardType="decimal-pad"
      />

      <Text style={styles.label}>Severity</Text>
      <View style={styles.severityButtons}>
        {['minor', 'medium', 'severe'].map((level) => (
          <TouchableOpacity
            key={level}
            style={[
              styles.severityButton,
              formData.severity === level && styles.severityButtonActive,
            ]}
            onPress={() => setFormData({ ...formData, severity: level })}
          >
            <Text style={styles.severityButtonText}>{level.toUpperCase()}</Text>
          </TouchableOpacity>
        ))}
      </View>

      <Text style={styles.label}>Description</Text>
      <TextInput
        style={[styles.input, styles.textarea]}
        placeholder="Enter description..."
        value={formData.description}
        onChangeText={(value) => setFormData({ ...formData, description: value })}
        multiline
        numberOfLines={4}
      />

      <TouchableOpacity
        style={[styles.submitButton, loading && styles.submitButtonDisabled]}
        onPress={handleSubmit}
        disabled={loading}
      >
        <Text style={styles.submitButtonText}>{loading ? 'Submitting...' : 'Submit Report'}</Text>
      </TouchableOpacity>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#333',
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    marginTop: 15,
    marginBottom: 8,
    color: '#333',
  },
  input: {
    backgroundColor: 'white',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
  },
  textarea: {
    textAlignVertical: 'top',
  },
  severityButtons: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 15,
  },
  severityButton: {
    flex: 1,
    paddingVertical: 12,
    marginHorizontal: 5,
    backgroundColor: '#e0e0e0',
    borderRadius: 8,
    alignItems: 'center',
  },
  severityButtonActive: {
    backgroundColor: '#1976d2',
  },
  severityButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#333',
  },
  submitButton: {
    backgroundColor: '#1976d2',
    paddingVertical: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
    marginBottom: 30,
  },
  submitButtonDisabled: {
    opacity: 0.5,
  },
  submitButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default ReportScreen;
