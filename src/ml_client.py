"""
MCP Client for interacting with ML models

This client connects to MCP servers and provides a simple interface
for running predictions and training models.
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MLClient:
    """Client for ML Model MCP Server."""
    
    def __init__(self, server_script: str = "src/mcp_server.py"):
        self.server_script = server_script
        self.session = None
    
    async def connect(self):
        """Connect to the MCP server."""
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
        """Run prediction on a model."""
        result = await self.session.call_tool(
            "predict",
            arguments={"model_name": model_name, "input_data": input_data}
        )
        return result
    
    async def train(self, model_name: str, training_data_path: str, epochs: int = 10):
        """Train a new model."""
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
        """List all available models."""
        result = await self.session.call_tool("list_models", arguments={})
        return result
    
    async def disconnect(self):
        """Disconnect from the server."""
        if self.session:
            await self.session.close()
        if hasattr(self, 'stdio_context'):
            await self.stdio_context.__aexit__(None, None, None)


async def main():
    """Example usage."""
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
