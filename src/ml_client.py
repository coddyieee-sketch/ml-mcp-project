"""
MCP Client for Interacting with ML Models
==========================================

This client provides a high-level Python interface for connecting to
ML model MCP servers. It handles connection management and exposes
simple async methods for model operations.

Features:
---------
- Automatic connection management
- Tool discovery
- Simple async API for predictions and training
- Error handling and reconnection support

Usage:
------
    from ml_client import MLClient
    
    client = MLClient()
    await client.connect()
    
    # List available models
    models = await client.list_models()
    
    # Run prediction
    result = await client.predict(
        model_name="my-model",
        input_data={"features": [1.0, 2.0, 3.0]}
    )
    
    await client.disconnect()
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MLClient:
    """
    Client for ML Model MCP Server.
    
    Provides a simple async interface for interacting with ML models
    exposed via MCP protocol. Handles connection lifecycle and tool calls.
    
    Attributes:
        server_script: Path to the MCP server script (default: src/mcp_server.py)
        session: Active MCP client session
    
    Example:
        client = MLClient()
        await client.connect()
        models = await client.list_models()
        await client.disconnect()
    """
    
    def __init__(self, server_script: str = "src/mcp_server.py"):
        """
        Initialize ML Client.
        
        Args:
            server_script: Path to the MCP server script to connect to
        """
        self.server_script = server_script
        self.session = None
    
    async def connect(self):
        """
        Establish connection to the MCP server.
        
        Starts the server process as a subprocess and initializes
        the MCP session. Lists available tools upon successful connection.
        
        Raises:
            ConnectionError: If unable to connect to the server
        """
        server_params = StdioServerParameters(
            command="python",
            args=[self.server_script]
        )
        
        self.stdio_context = stdio_client(server_params)
        self.read, self.write = await self.stdio_context.__aenter__()
        self.session = ClientSession(self.read, self.write)
        await self.session.initialize()
        
        # List available tools
        tools = await self.session.list_tools()
        print(f"Connected! Available tools: {[t.name for t in tools.tools]}")
    
    async def predict(self, model_name: str, input_data: dict):
        """
        Run inference on a trained model.
        
        Args:
            model_name: Name of the model to use for prediction
            input_data: Dictionary containing input features/data
        
        Returns:
            Prediction results including predicted values and confidence scores
        
        Example:
            result = await client.predict(
                model_name="classifier",
                input_data={"features": [0.5, 0.8, 0.2]}
            )
        """
        result = await self.session.call_tool(
            "predict",
            arguments={"model_name": model_name, "input_data": input_data}
        )
        return result
    
    async def train(self, model_name: str, training_data_path: str, epochs: int = 10):
        """
        Train a new ML model.
        
        Args:
            model_name: Name to assign to the newly trained model
            training_data_path: Path to the training dataset
            epochs: Number of training iterations (default: 10)
        
        Returns:
            Training status and metadata
        
        Example:
            result = await client.train(
                model_name="my-classifier",
                training_data_path="data/train.csv",
                epochs=50
            )
        """
        result = await self.session.call_tool(
            "train",
            arguments={
                "model_name": model_name,
                "training_data_path": training_data_path,
                "epochs": epochs
            }
        )
        return result
    
    async def list_models(self):
        """
        List all trained models available on the server.
        
        Returns:
            Dictionary containing list of available models with metadata
        
        Example:
            models = await client.list_models()
            print(f"Available models: {models['models']}")
        """
        result = await self.session.call_tool("list_models", arguments={})
        return result
    
    async def disconnect(self):
        """
        Close connection to the MCP server.
        
        Properly closes the session and cleans up resources.
        Should be called when done using the client.
        """
        if self.session:
            await self.session.close()
        if hasattr(self, 'stdio_context'):
            await self.stdio_context.__aexit__(None, None, None)


async def main():
    """
    Example usage demonstrating client capabilities.
    
    Shows how to connect, list models, and interact with the MCP server.
    Uncomment the prediction example to test with actual models.
    """
    client = MLClient()
    
    try:
        await client.connect()
        
        # List available models
        models = await client.list_models()
        print(f"Models: {models}")
        
        # Example prediction
        # prediction = await client.predict(
        #     model_name="my-model",
        #     input_data={"features": [1.0, 2.0, 3.0]}
        # )
        # print(f"Prediction: {prediction}")
        
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
