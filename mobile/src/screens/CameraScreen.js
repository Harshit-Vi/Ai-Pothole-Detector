import React, { useState, useRef } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native';
import { RNCamera } from 'react-native-camera';
import axios from 'axios';

const CameraScreen = () => {
  const [loading, setLoading] = useState(false);
  const cameraRef = useRef(null);
  const apiBaseUrl = process.env.REACT_NATIVE_API_BASE_URL || 'http://localhost:5000/api';

  const takePicture = async () => {
    if (cameraRef.current) {
      setLoading(true);
      try {
        const data = await cameraRef.current.takePictureAsync({
          quality: 0.8,
          base64: true,
        });
        
        // Send to backend for detection
        const formData = new FormData();
        formData.append('image', {
          uri: data.uri,
          type: 'image/jpeg',
          name: 'pothole_detection.jpg',
        });

        const response = await axios.post(`${apiBaseUrl}/detect/image`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });

        console.log('Detection result:', response.data);
        // TODO: Handle detection results
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <View style={styles.container}>
      <RNCamera
        ref={cameraRef}
        style={styles.camera}
        type={RNCamera.Constants.Type.back}
        flashMode={RNCamera.Constants.FlashMode.on}
        permissionDialogTitle="Permission to use camera"
        permissionDialogMessage="We need your permission to use your camera"
      >
        <View style={styles.bottomBar}>
          <TouchableOpacity onPress={takePicture} disabled={loading}>
            <View style={styles.captureButton}>
              {loading ? (
                <ActivityIndicator size="large" color="#fff" />
              ) : (
                <Text style={styles.captureButtonText}>Capture</Text>
              )}
            </View>
          </TouchableOpacity>
        </View>
      </RNCamera>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  camera: {
    flex: 1,
  },
  bottomBar: {
    flex: 0,
    flexDirection: 'row',
    justifyContent: 'center',
    paddingVertical: 20,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  captureButton: {
    width: 70,
    height: 70,
    borderRadius: 35,
    backgroundColor: '#FF6B6B',
    justifyContent: 'center',
    alignItems: 'center',
  },
  captureButtonText: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
});

export default CameraScreen;
