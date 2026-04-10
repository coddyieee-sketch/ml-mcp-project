"""
Model Training Example
=======================

This example demonstrates how to train a new ML model using the MCP server.

Prerequisites:
--------------
1. Start the MCP server: python src/mcp_server.py
2. Have training data ready in the data/ directory

Usage:
------
    python examples/model_training.py
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ml_client import MLClient


async def main():
    """Run model training example."""
    
    client = MLClient()
    
    try:
        # Connect to the MCP server
        print("🔌 Connecting to MCP server...")
        await client.connect()
        print("✅ Connected!\n")
        
        # Start training
        print("🚀 Starting model training...")
        result = await client.train(
            model_name="my-custom-model",
            training_data_path="data/training_data.csv",
            epochs=100
        )
        
        print(f"   Status: {result.get('status', 'unknown')}")
        print(f"   Model: {result.get('model', 'unknown')}")
        print(f"   Epochs: {result.get('epochs', 0)}")
        print(f"   Data: {result.get('data_path', 'unknown')}")
        print()
        
        # Check if model is now available
        print("📋 Verifying model availability...")
        models = await client.list_models()
        model_names = [m['name'] for m in models.get('models', [])]
        
        if "my-custom-model" in str(model_names):
            print("   ✅ Model successfully trained and available!")
        else:
            print("   ⏳ Model training in progress or needs verification")
        
        print(f"\n   All models: {model_names}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Make sure:")
        print("   - MCP server is running: python src/mcp_server.py")
        print("   - Training data exists at the specified path")
    finally:
        # Always disconnect cleanly
        print("\n👋 Disconnecting...")
        await client.disconnect()
        print("✅ Disconnected!")


if __name__ == "__main__":
    asyncio.run(main())
