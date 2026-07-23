import { RNCamera } from 'react-native-camera';

export const takePicture = async (cameraRef) => {
  if (cameraRef) {
    try {
      const data = await cameraRef.takePictureAsync({
        quality: 0.8,
        base64: false,
        fixOrientation: true,
      });
      return data;
    } catch (error) {
      console.error('Camera error:', error);
      throw error;
    }
  }
};

export const recordVideo = async (cameraRef, maxDuration = 30000) => {
  if (cameraRef) {
    try {
      const data = await cameraRef.recordAsync({
        maxDuration: maxDuration / 1000, // Convert to seconds
        quality: RNCamera.Constants.VideoQuality['480p'],
      });
      return data;
    } catch (error) {
      console.error('Video recording error:', error);
      throw error;
    }
  }
};
