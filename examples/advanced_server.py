"""
Advanced MCP Server Example

This example demonstrates more advanced features of the MCP protocol,
including complex data types, error handling, and async tools.
"""

from mcp.server.fastmcp import FastMCP, Context, Image
from typing import List, Dict, Optional
import asyncio
import platform
import random
from datetime import datetime
from pathlib import Path

# Create an MCP server with dependencies
mcp = FastMCP(
    "Advanced Demo",
    description="An advanced MCP server demonstrating various features",
    dependencies=["pillow", "httpx"]
)

# ---- TOOLS ----

@mcp.tool()
def calculator(operation: str, a: float, b: float) -> Dict[str, float]:
    """
    Perform a mathematical operation on two numbers.
    
    Args:
        operation: One of "add", "subtract", "multiply", "divide"
        a: First number
        b: Second number
        
    Returns:
        Dictionary with result and input values
    """
    result = None
    
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }

@mcp.tool()
async def delayed_echo(message: str, delay_seconds: float = 1.0) -> str:
    """
    Echo a message after a specified delay.
    
    Args:
        message: The message to echo
        delay_seconds: How long to wait before responding
        
    Returns:
        The original message with timestamp
    """
    await asyncio.sleep(delay_seconds)
    now = datetime.now().strftime("%H:%M:%S")
    return f"[{now}] {message}"

@mcp.tool()
def analyze_text(text: str, ctx: Context) -> Dict[str, any]:
    """
    Analyze text and return statistics.
    
    Args:
        text: The text to analyze
        
    Returns:
        Dictionary with text statistics
    """
    # Report progress
    ctx.info("Starting text analysis...")
    
    words = text.split()
    char_count = len(text)
    word_count = len(words)
    
    # Calculate word frequencies
    word_freq = {}
    for word in words:
        word = word.lower().strip(".,!?;:()")
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Find most common words
    common_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
    
    ctx.info("Analysis complete!")
    
    return {
        "character_count": char_count,
        "word_count": word_count,
        "average_word_length": sum(len(word) for word in words) / max(1, word_count),
        "most_common_words": dict(common_words),
        "sentence_count": text.count('.') + text.count('!') + text.count('?')
    }

# ---- RESOURCES ----

@mcp.resource("system://details")
def system_details() -> Dict[str, any]:
    """Get detailed system information"""
    return {
        "os": platform.system(),
        "version": platform.version(),
        "python": platform.python_version(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "node": platform.node(),
        "time": datetime.now().isoformat()
    }

@mcp.resource("quotes://random")
def random_quote() -> Dict[str, str]:
    """Get a random inspirational quote"""
    quotes = [
        {"text": "Be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
        {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
        {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
        {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"}
    ]
    return random.choice(quotes)

@mcp.resource("weather://{city}")
def get_weather(city: str) -> Dict[str, any]:
    """
    Get simulated weather for a city.
    
    Args:
        city: The name of the city
        
    Returns:
        Weather information
    """
    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Thunderstorms", "Snowy", "Foggy"]
    temp = random.randint(-10, 35)
    humidity = random.randint(30, 95)
    wind_speed = random.randint(0, 30)
    
    return {
        "city": city,
        "temperature": {
            "celsius": temp,
            "fahrenheit": (temp * 9/5) + 32
        },
        "condition": random.choice(conditions),
        "humidity": humidity,
        "wind_speed": wind_speed,
        "forecast": [
            {"day": "Today", "high": temp, "low": temp - random.randint(5, 15), "condition": random.choice(conditions)},
            {"day": "Tomorrow", "high": temp + random.randint(-5, 5), "low": temp - random.randint(5, 15), "condition": random.choice(conditions)},
            {"day": "Day after", "high": temp + random.randint(-8, 8), "low": temp - random.randint(5, 15), "condition": random.choice(conditions)}
        ]
    }

# ---- PROMPTS ----

@mcp.prompt()
def analyze_prompt(text: str) -> str:
    """Create a prompt for text analysis"""
    return f"""Please analyze this text and provide insights:

{text}

Consider elements like tone, style, key themes, and any notable patterns."""

if __name__ == "__main__":
    # This allows running the server directly
    mcp.run() 