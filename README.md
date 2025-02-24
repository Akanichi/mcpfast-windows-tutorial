# Testing mcpfast with Claude Desktop on Windows

This tutorial will guide you through setting up and testing mcpfast (Model Context Protocol) with Claude Desktop on Windows.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Prerequisites

Before you begin, make sure you have:

1. **Windows 10/11** operating system
2. **[uv](https://github.com/astral-sh/uv)** installed (Python package manager)
3. **[Claude Desktop](https://claude.ai/download)** installed
4. **Python 3.10+** installed

## Step 1: Set Up Your Environment

First, create a new directory for your project and set up a virtual environment:

```powershell
# Create a project directory
mkdir mcpserver
cd mcpserver

# Create a virtual environment
uv venv

# Activate the virtual environment
.venv\Scripts\activate
```

## Step 2: Install MCP SDK

Install the MCP SDK with CLI tools:

```powershell
uv pip install "mcp[cli]"
```

Or install from the requirements.txt file:

```powershell
uv pip install -r requirements.txt
```

## Step 3: Create a Simple MCP Server

Create a file named `test_server.py` with the following content:

```python
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
```

This server provides:
- Two calculator tools: `add` and `multiply`
- A greeting resource that returns a personalized greeting
- A system info resource that returns information about your system

## Step 4: Test Your Server (Optional)

You can test your server with the MCP Inspector before installing it in Claude Desktop:

```powershell
mcp dev test_server.py
```

This will start a web interface at http://localhost:5173 where you can interact with your server.

## Step 5: Install Your Server in Claude Desktop

Install your server in Claude Desktop:

```powershell
mcp install test_server.py
```

You should see a success message: `Successfully installed Test Server in Claude app`

## Step 6: Using Your MCP Server with Claude

1. Open Claude Desktop
2. Start a new conversation
3. Click on the "+" button in the bottom left corner
4. Select "Test Server" from the list of available servers
5. Now you can interact with Claude using your custom tools and resources

### Example Interactions

Try asking Claude to:

- **Use the calculator tools:**
  "Can you add 5 and 7 using the calculator tool?"
  "What's 12 multiplied by 8?"

- **Get a personalized greeting:**
  "Can you get a greeting for John?"

- **Retrieve system information:**
  "What's my system information?"

## Advanced Example

This repository also includes an advanced example in `examples/advanced_server.py` that demonstrates:

- Complex data types and return values
- Asynchronous tools
- Error handling
- Progress reporting
- Multiple resource types
- Custom prompts

To try the advanced example:

```powershell
mcp install examples/advanced_server.py
```

Then in Claude Desktop, you can:

- Use the calculator with various operations
- Get simulated weather for any city
- Analyze text with detailed statistics
- Get random inspirational quotes
- Use delayed echo with custom timing
- Access detailed system information

## Troubleshooting

If you encounter any issues:

1. Make sure Claude Desktop is running and up to date
2. Check that the server was installed correctly
3. Try restarting Claude Desktop
4. If needed, uninstall and reinstall the server:
   ```powershell
   mcp uninstall "Test Server"
   mcp install test_server.py
   ```

## Creating More Advanced Servers

You can extend your server by:

1. **Adding more tools:**
   ```python
   @mcp.tool()
   def divide(a: float, b: float) -> float:
       """Divide two numbers"""
       if b == 0:
           return "Cannot divide by zero"
       return a / b
   ```

2. **Adding more resources:**
   ```python
   @mcp.resource("weather://{city}")
   def get_weather(city: str) -> str:
       """Get weather for a city (simulated)"""
       import random
       conditions = ["sunny", "cloudy", "rainy", "snowy"]
       temp = random.randint(0, 30)
       condition = random.choice(conditions)
       return f"Weather in {city}: {condition}, {temp}°C"
   ```

3. **Using more complex data types:**
   ```python
   @mcp.tool()
   def analyze_text(text: str) -> dict:
       """Analyze text and return statistics"""
       words = text.split()
       return {
           "word_count": len(words),
           "character_count": len(text),
           "average_word_length": sum(len(word) for word in words) / len(words) if words else 0
       }
   ```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [Claude Desktop Download](https://claude.ai/download)
- [uv Documentation](https://github.com/astral-sh/uv)

Happy coding with Claude and MCP! 