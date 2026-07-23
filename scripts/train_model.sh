#!/bin/bash
# Model training script

echo "Starting model training..."

cd training

# Create datasets directory
mkdir -p datasets/{train,val,test}/{images,labels}

# Download dataset
echo "Downloading RDD2020 dataset...
python dataset_download.py

# Start training
echo "Training YOLOv8 model...
python train_model.py

echo "Training completed!
