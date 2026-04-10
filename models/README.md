# Models Directory

This directory stores trained ML model files.

## Supported Model Formats

| Format | Extension | Framework |
|--------|-----------|-----------|
| PyTorch | `.pth`, `.pt` | PyTorch |
| Keras | `.h5`, `.keras` | TensorFlow/Keras |
| Scikit-learn | `.pkl`, `.joblib` | Scikit-learn |
| ONNX | `.onnx` | ONNX (cross-framework) |
| TensorFlow | `.pb` | TensorFlow |
| Pickle | `.pkl` | Python (generic) |

## Model Naming Convention

Use descriptive names:

```
models/
├── image-classifier-resnet50.pth
├── text-sentiment-bert.h5
├── fraud-detection-xgboost.pkl
└── regression-linear.onnx
```

## Loading Models

### PyTorch

```python
import torch

model = torch.load("models/my-model.pth")
model.eval()

with torch.no_grad():
    output = model(input_tensor)
```

### Scikit-learn

```python
import joblib

model = joblib.load("models/my-model.pkl")
predictions = model.predict(X_test)
```

### TensorFlow/Keras

```python
from tensorflow import keras

model = keras.models.load_model("models/my-model.h5")
predictions = model.predict(X_test)
```

### ONNX

```python
import onnxruntime as ort

session = ort.InferenceSession("models/my-model.onnx")
outputs = session.run(None, {"input": input_data})
```

## Model Versioning

Consider versioning your models:

```
models/
├── v1/
│   └── classifier-v1.0.pth
├── v2/
│   └── classifier-v2.0.pth
└── latest/
    └── classifier.pth  # Symlink to latest
```

## Model Metadata

Consider adding a `metadata.json` for each model:

```json
{
  "name": "image-classifier",
  "version": "1.0.0",
  "framework": "pytorch",
  "trained_on": "2026-04-10",
  "accuracy": 0.95,
  "classes": ["cat", "dog", "bird"],
  "input_shape": [3, 224, 224]
}
```

## Security

⚠️ **Warning**: Only load models from trusted sources. Malicious pickle files can execute arbitrary code.

For production:
- Validate model signatures
- Use read-only permissions
- Scan for vulnerabilities
