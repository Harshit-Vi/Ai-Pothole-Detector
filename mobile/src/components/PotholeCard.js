import React from 'react';
import { View, StyleSheet } from 'react-native';

const PotholeCard = ({ pothole }) => {
  return (
    <View style={styles.card}>
      <View style={styles.header}>
        <Text style={styles.title}>{pothole.address}</Text>
      </View>
      <View style={styles.body}>
        <Text style={styles.detail}>Severity: {pothole.severity}</Text>
        <Text style={styles.detail}>Location: {pothole.latitude.toFixed(4)}, {pothole.longitude.toFixed(4)}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: 'white',
    borderRadius: 8,
    marginBottom: 10,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 3.84,
    elevation: 5,
  },
  header: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  body: {
    padding: 15,
  },
  detail: {
    fontSize: 14,
    marginBottom: 5,
    color: '#666',
  },
});

export default PotholeCard;
