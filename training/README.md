# AI Pothole Detector - Training Documentation

## Dataset Preparation

The system uses the RDD2020 (Road Damage Detection 2020) dataset which contains 9,000+ annotated pothole images.

### Dataset Structure

```
datasets/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

## Model Training

### Prerequisites

```bash
pip install -r requirements.txt
```

### Training Steps

1. **Download Dataset**

```bash
python dataset_download.py
```

2. **Prepare Data**

Create `data.yaml` file:

```yaml
path: ./datasets
train: train/images
val: val/images
test: test/images

nc: 1
names: ['pothole']
```

3. **Start Training**

```bash
python train_model.py
```

### Training Configuration

- **Model**: YOLOv8 Nano (yolov8n.pt)
- **Epochs**: 100
- **Batch Size**: 32
- **Image Size**: 640x640
- **Device**: GPU (CUDA)

## Model Evaluation

After training, evaluate on validation set:

```bash
python train_model.py  # Run evaluation
```

## Model Export

Export trained model to different formats:

- PyTorch (.pt)
- ONNX (.onnx)
- TensorFlow Lite (.tflite)
- TensorFlow SavedModel (.pb)

## Expected Performance

- **mAP@0.5**: > 85%
- **mAP@0.5:0.95**: > 75%
- **Inference Speed**: < 100ms per image
