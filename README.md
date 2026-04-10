# ML MCP Project

An AI/ML project with Model Context Protocol (MCP) integration for standardized model serving and tool access.

## Features

- 🤖 **MCP Server** - Expose ML models as MCP tools
- 🔌 **MCP Client** - Easy client for model inference and training
- 📦 **Model Management** - Organized model storage and versioning
- 🧪 **Testing** - Built-in test framework

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

## Usage

### Start the MCP Server

```bash
python src/mcp_server.py
```

### Use the Client

```bash
python src/ml_client.py
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

## Adding Your ML Model

1. Train your model and save it in `models/`
2. Update `mcp_server.py` to load your model
3. Implement prediction logic in the `call_tool` handler
4. Test with the client

## MCP Integration

This project uses the [Model Context Protocol](https://modelcontextprotocol.io/) to standardize how AI models are exposed and consumed. MCP allows:

- **Interoperability** - Any MCP-compatible client can use your models
- **Tool Discovery** - Clients can discover available models and capabilities
- **Standard Interface** - Consistent API for prediction, training, and management

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
