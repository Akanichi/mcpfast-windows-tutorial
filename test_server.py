"""
Simple MCP Test Server

A basic MCP server with a calculator tool and a greeting resource.
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Test Server")

# Add a calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add a greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Add a system info resource
@mcp.resource("system://info")
def get_system_info() -> dict:
    """Get system information"""
    import platform
    return {
        "os": platform.system(),
        "version": platform.version(),
        "python": platform.python_version()
    } 