"""FeedOracle MCP Client for seed generation."""
import httpx, json, os, uuid
from typing import Optional

class FeedOracleMCP:
    def __init__(self, endpoint="https://mcp.feedoracle.io/mcp", api_key=None):
        self.endpoint = endpoint
        self.api_key = api_key or os.getenv("FEEDORACLE_API_KEY")
        self.session_id = None
        self.client = httpx.Client(timeout=30.0)

    def _call(self, method, params=None):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self.session_id: headers["Mcp-Session-Id"] = self.session_id
        r = self.client.post(self.endpoint, json={"jsonrpc":"2.0","id":str(uuid.uuid4())[:8],"method":method,"params":params or {}}, headers=headers)
        if "mcp-session-id" in r.headers: self.session_id = r.headers["mcp-session-id"]
        return r.json()

    def initialize(self):
        return self._call("initialize", {"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"mirofish-seed","version":"1.0"}})

    def list_tools(self):
        return self._call("tools/list").get("result",{}).get("tools",[])

    def call_tool(self, name, arguments=None):
        args = arguments or {}
        if self.api_key: args["api_key"] = self.api_key
        r = self._call("tools/call", {"name": name, "arguments": args})
        content = r.get("result",{}).get("content",[{}])
        return json.loads(content[0]["text"]) if content and content[0].get("text") else r

    def close(self): self.client.close()

def quick_call(endpoint, tool, args=None, api_key=None):
    c = FeedOracleMCP(endpoint, api_key); c.initialize(); r = c.call_tool(tool, args or {}); c.close(); return r
