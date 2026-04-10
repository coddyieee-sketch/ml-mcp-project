# ML MCP Project

An AI/ML project with **Model Context Protocol (MCP)** integration for standardized model serving and tool access.

## 📖 Overview

This project provides a complete framework for exposing machine learning models via the Model Context Protocol (MCP), enabling:

- **Interoperability**: Any MCP-compatible client can discover and use your models
- **Standardization**: Consistent API for prediction, training, and model management  
- **Tool Discovery**: Clients automatically discover available models and capabilities
- **Easy Integration**: Simple Python client library for quick integration

## 🎯 Use Cases

- Serve trained models as standardized tools for AI agents
- Enable multiple clients to access the same ML models
- Build ML-powered MCP servers for Claude, Codex, or other AI assistants
- Create reusable model inference pipelines

## ✨ Features

- 🤖 **MCP Server** - Expose ML models as discoverable MCP tools (predict, train, list_models)
- 🔌 **MCP Client** - High-level Python client for easy model inference and training
- 📦 **Model Management** - Organized model storage with automatic discovery
- 🧪 **Testing Framework** - Built-in pytest setup for unit and integration tests
- 📚 **Documentation** - Comprehensive docstrings and usage examples

## Project Structure

```
ml-mcp-project/
├── src/
│   ├── mcp_server.py    # MCP server exposing ML tools
│   ├── ml_client.py     # Client for interacting with models
│   └── __init__.py
├── models/              # Trained model files
├── data/                # Training and test data
├── tests/               # Unit and integration tests
├── requirements.txt     # Python dependencies
└── README.md
```

## Installation

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### Start the MCP Server

The MCP server exposes your ML models as tools that can be called by any MCP-compatible client:

```bash
# Activate virtual environment first
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Start the server
python src/mcp_server.py
```

The server runs on stdio and communicates via the MCP protocol.

### Use the Client

The client library provides a simple async interface:

```bash
# Run the example client
python src/ml_client.py
```

### Programmatic Usage

```python
from src.ml_client import MLClient
import asyncio

async def main():
    client = MLClient()
    await client.connect()
    
    # List available models
    models = await client.list_models()
    print(f"Available models: {models}")
    
    # Run prediction
    prediction = await client.predict(
        model_name="my-classifier",
        input_data={"features": [1.0, 2.0, 3.0, 4.0]}
    )
    print(f"Prediction: {prediction}")
    
    # Train a new model
    result = await client.train(
        model_name="new-model",
        training_data_path="data/training.csv",
        epochs=50
    )
    print(f"Training: {result}")
    
    await client.disconnect()

asyncio.run(main())
```

### Example Code

```python
from src.ml_client import MLClient
import asyncio

async def main():
    client = MLClient()
    await client.connect()
    
    # List models
    models = await client.list_models()
    print(models)
    
    # Run prediction
    result = await client.predict(
        model_name="my-model",
        input_data={"features": [1.0, 2.0, 3.0]}
    )
    print(result)
    
    await client.disconnect()

asyncio.run(main())
```

## 🧠 Adding Your ML Model

### Step 1: Save Your Trained Model

Place your trained model file in the `models/` directory:

```
models/
├── my-classifier.pth      # PyTorch model
├── my-regressor.h5        # Keras/TensorFlow model
├── my-processor.pkl       # Scikit-learn model
└── my-model.onnx          # ONNX format
```

### Step 2: Update the MCP Server

Edit `src/mcp_server.py` to load and use your model:

```python
# Add model loading at module level
import torch

class MyClassifier:
    def __init__(self):
        self.model = torch.load("models/my-classifier.pth")
        self.model.eval()
    
    def predict(self, input_data):
        with torch.no_grad():
            tensor = torch.tensor(input_data["features"])
            output = self.model(tensor)
            return output.tolist()

classifier = MyClassifier()

# Update the predict tool handler
if name == "predict":
    model_name = arguments.get("model_name")
    input_data = arguments.get("input_data")
    
    if model_name == "my-classifier":
        prediction = classifier.predict(input_data)
        result = {
            "model": model_name,
            "prediction": prediction,
            "confidence": float(max(prediction))
        }
    # ... handle other models
```

### Step 3: Test Your Integration

```python
from src.ml_client import MLClient

client = MLClient()
await client.connect()

# Test prediction
result = await client.predict(
    model_name="my-classifier",
    input_data={"features": [0.5, 0.8, 0.2, 0.9]}
)
print(result)

await client.disconnect()
```

## 🔗 MCP Integration

This project uses the **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)** to standardize how AI models are exposed and consumed.

### What is MCP?

MCP is an open protocol that standardizes how applications provide context and tools to AI systems. It enables:

- **Tool Discovery**: AI clients can query what tools/models are available
- **Structured Interaction**: Consistent request/response format
- **Interoperability**: Works with any MCP-compatible client (Claude Desktop, Codex, etc.)
- **Security**: Clear boundaries and permission models

### Architecture

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  MCP Client     │ ◄─────► │  MCP Server      │ ◄─────► │  ML Models      │
│  (AI Assistant) │  MCP    │  (mcp_server.py) │  Loads │  (models/)      │
└─────────────────┘  Proto  └──────────────────┘        └─────────────────┘
```

### Available Tools

| Tool | Description | Input | Output |
|------|-------------|-------|--------|
| `predict` | Run inference on a model | model_name, input_data | prediction, confidence |
| `train` | Train a new model | model_name, data_path, epochs | status, metadata |
| `list_models` | List available models | (none) | list of models |

### Connecting to AI Assistants

To use this server with Claude Desktop or other MCP clients, add to your MCP config:

```json
{
  "mcpServers": {
    "ml-models": {
      "command": "python",
      "args": ["/path/to/ml-mcp-project/src/mcp_server.py"]
    }
  }
}
```

## Development

```bash
# Run tests
pytest tests/

# Format code
black src/ tests/

# Lint
flake8 src/ tests/
```

## License

MIT
