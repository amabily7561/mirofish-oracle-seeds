#!/usr/bin/env python3
"""MiroFish Seed Generator — Powered by 484 FeedOracle MCP Tools"""
import argparse, json, os, sys
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "connectors"))
from feedoracle_mcp import FeedOracleMCP, quick_call
from oracle_registry import ORACLES

SCENARIOS = {
    "usdt_mica_ban": {
        "title": "USDT Loses MiCA License — Market Cascade",
        "prompt": "ESMA announces USDT fails MiCA. Delisted from EU exchanges in 30 days. Simulate 60-day market reaction.",
        "tools": [("feedoracle_core","mica_status",{"token_symbol":"USDT"}),("feedoracle_core","mica_status",{"token_symbol":"USDC"}),("feedoracle_core","peg_deviation",{"token_symbol":"USDT"}),("feedoracle_core","significant_issuer",{"token_symbol":"USDT"}),("feedoracle_core","reserve_quality",{"token_symbol":"USDT"}),("feedoracle_core","macro_risk",{})],
        "agents": 5000,
    },
    "dora_enforcement": {
        "title": "DORA Enforcement Wave — Banks Under Pressure",
        "prompt": "BaFin issues first DORA enforcement notices to 12 German banks. Fines up to EUR 5M. Simulate 90-day reaction.",
        "tools": [("ampel","readiness_check",{"entity_id":"demo_bank"}),("ampel","readiness_check",{"entity_id":"demo_versicherung"}),("ampel","gap_report",{"entity_id":"demo_bank"})],
        "agents": 3000,
    },
    "stablecoin_bankrun": {
        "title": "Stablecoin Bank Run — Contagion",
        "prompt": "USDT depegs to $0.94. Binance pauses withdrawals. Simulate 14-day contagion across DeFi.",
        "tools": [("feedoracle_core","peg_deviation",{"token_symbol":"USDT"}),("feedoracle_core","peg_deviation",{"token_symbol":"USDC"}),("feedoracle_core","evidence_leaderboard",{"top_n":20}),("feedoracle_core","macro_risk",{})],
        "agents": 10000,
    },
    "fed_rate_shock": {
        "title": "Fed Emergency Rate Cut — Crypto Impact",
        "prompt": "Fed cuts 75bps emergency. Treasury yields collapse. Simulate impact on tokenized assets over 30 days.",
        "tools": [("feedoracle_core","macro_risk",{})],
        "agents": 5000,
    },
    "eu_stablecoin_purge": {
        "title": "EU Purges Non-Compliant Stablecoins",
        "prompt": "Only USDC, EURC, RLUSD approved under MiCA. All others cease trading in EU in 60 days.",
        "tools": [("feedoracle_core","mica_status",{"token_symbol":"USDT"}),("feedoracle_core","mica_status",{"token_symbol":"USDC"}),("feedoracle_core","mica_status",{"token_symbol":"EURC"}),("feedoracle_core","mica_status",{"token_symbol":"RLUSD"}),("feedoracle_core","compliance_preflight",{"token_symbol":"USDT"})],
        "agents": 8000,
    },
}

def generate(scenario_key, api_key=None):
    s = SCENARIOS[scenario_key]
    print(f"\n  Generating: {s['title']}")
    data = []
    for oracle_key, tool, args in s["tools"]:
        endpoint = ORACLES.get(oracle_key, {}).get("url", "https://mcp.feedoracle.io/mcp")
        print(f"  → {tool}...", end=" ")
        try:
            r = quick_call(endpoint, tool, args, api_key)
            data.append({"tool": tool, "result": r})
            print("✓")
        except Exception as e:
            print(f"✗ {e}")

    seed = f"# MiroFish Seed: {s['title']}\n\n## Prompt\n{s['prompt']}\n\n## Config\n- Agents: {s['agents']}\n- Generated: {datetime.utcnow().isoformat()}Z\n- Source: FeedOracle (484 MCP tools)\n\n## Data\n\n"
    for d in data:
        seed += f"### {d['tool']}\n```json\n{json.dumps(d['result'],indent=2,default=str)[:2000]}\n```\n\n"

    out = f"seed_{scenario_key}_{datetime.utcnow().strftime('%Y%m%d')}.md"
    with open(out, "w") as f: f.write(seed)
    print(f"\n  Saved: {out} ({len(seed):,} chars)")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--scenario", "-s")
    p.add_argument("--api-key", "-k")
    p.add_argument("--list", "-l", action="store_true")
    a = p.parse_args()
    if a.list or not a.scenario:
        for k, s in SCENARIOS.items(): print(f"  {k:25s} {s['title']}")
    else:
        generate(a.scenario, a.api_key)
