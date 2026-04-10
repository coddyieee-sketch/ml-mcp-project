"""
Basic Prediction Example
=========================

This example demonstrates how to use the ML MCP client to run predictions
on trained models.

Prerequisites:
--------------
1. Start the MCP server: python src/mcp_server.py
2. Have at least one trained model in the models/ directory

Usage:
------
    python examples/basic_prediction.py
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ml_client import MLClient


async def main():
    """Run prediction examples."""
    
    client = MLClient()
    
    try:
        # Connect to the MCP server
        print("🔌 Connecting to MCP server...")
        await client.connect()
        print("✅ Connected!\n")
        
        # List available models
        print("📋 Available models:")
        models = await client.list_models()
        print(f"   Found {models.get('count', 0)} models")
        for model in models.get('models', []):
            print(f"   - {model['name']} ({model['type']})")
        print()
        
        # Example 1: Simple prediction
        print("🔮 Running prediction example...")
        prediction = await client.predict(
            model_name="example-model",
            input_data={
                "features": [0.5, 0.8, 0.2, 0.9, 0.1],
                "metadata": {"source": "example_script"}
            }
        )
        print(f"   Result: {prediction}")
        print()
        
        # Example 2: Batch prediction (if supported by your model)
        print("📊 Running batch prediction...")
        batch_result = await client.predict(
            model_name="example-model",
            input_data={
                "batch": [
                    [0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6],
                    [0.7, 0.8, 0.9]
                ]
            }
        )
        print(f"   Result: {batch_result}")
        print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Make sure the MCP server is running: python src/mcp_server.py")
    finally:
        # Always disconnect cleanly
        print("👋 Disconnecting...")
        await client.disconnect()
        print("✅ Disconnected!")


if __name__ == "__main__":
    asyncio.run(main())
