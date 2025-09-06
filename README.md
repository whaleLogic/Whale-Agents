# AI Agents 🤖 with OpenAI 🧰 Tool Calling

### This repository contains basic AI agents built using the OpenAI API

📦 Getting Started

1. Clone the repo
2. Set up environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```
㊙️ Create a .env file with your API key:
```
OPENAI_API_KEY=sk-xxxxxx
```
3. Run an example
```
python examples/stock_agent.py
```

### 🧰 Tool Definition and Usage 
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the latest stock price for a ticker symbol.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string"}
                },
                "required": ["symbol"]
            },
        },
    }
]

def get_stock_price(symbol: str):
    # Realtime API logic replaces dummy data
    prices = {"AAPL": 174.2, "TSLA": 259.3}
    return {"symbol": symbol, "price": prices.get(symbol, "N/A")}

```

#### Define more tools with the JSON schema 😆
