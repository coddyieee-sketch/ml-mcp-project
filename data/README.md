# Data Directory

This directory contains training and test datasets for ML models.

## Structure

```
data/
├── README.md           # This file
├── training/           # Training datasets
│   ├── train.csv
│   └── train_labels.csv
├── test/              # Test datasets
│   └── test.csv
└── raw/               # Raw/unprocessed data
    └── raw_data.csv
```

## Supported Formats

- **CSV**: `.csv` files for tabular data
- **JSON**: `.json` files for structured data
- **Parquet**: `.parquet` for large datasets
- **NumPy**: `.npy` arrays
- **Pickle**: `.pkl` for Python objects

## Adding Your Data

1. Place your dataset in the appropriate subdirectory
2. Update data loading code in `src/mcp_server.py`
3. Document the dataset format and schema

## Example Dataset Structure

### Training Data (CSV)

```csv
feature_1,feature_2,feature_3,label
0.5,0.8,0.2,1
0.3,0.1,0.9,0
0.7,0.6,0.4,1
```

### Loading in Python

```python
import pandas as pd

# Load training data
df = pd.read_csv("data/training/train.csv")
X = df.drop('label', axis=1).values
y = df['label'].values
```

## Data Preprocessing

Consider adding preprocessing scripts:

```bash
data/
├── preprocess.py       # Data cleaning and normalization
└── augment.py          # Data augmentation
```

## Privacy & Security

⚠️ **Important**: Never commit sensitive or private data to Git.

- Add large datasets to `.gitignore`
- Use `.gitkeep` as placeholders
- Store sensitive data externally and load via paths
