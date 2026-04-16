# 🐟 MiroFish × FeedOracle — Real-Time Oracle Data for Swarm Predictions

> **484 MCP tools** feeding live compliance, market, macro, and intelligence data into MiroFish simulations.
> Every prediction grounded in cryptographically signed, evidence-grade data.

[![MCP Tools](https://img.shields.io/badge/MCP_Tools-484-brightgreen)](https://mcp.feedoracle.io)
[![Oracles](https://img.shields.io/badge/Oracles-44_Servers-blue)](https://feedoracle.io)
[![MiCA](https://img.shields.io/badge/MiCA-105%2B_Stablecoins-orange)](https://feedoracle.io/ampel/)
[![DORA](https://img.shields.io/badge/DORA-22_Assessment_Tools-red)](https://feedoracle.io/ampel/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## The Problem

MiroFish simulations are only as good as their seed data. Most users paste news articles — **unstructured, unverified, stale**.

What if your 10,000 simulated agents had access to:
- Real-time stablecoin peg deviations (MiCA Art. 35)
- Live reserve quality scores (MiCA Art. 24/25)
- Macro economic risk composites (86 FRED series)
- Sanctions screening results (EU/OFAC/UN)
- DEX liquidity depth analysis
- Carbon footprint per blockchain
- Cryptographically signed evidence bundles

**This repo connects MiroFish to 484 MCP tools across 44 oracle servers.**

---

## Quick Start

```bash
pip install -r requirements.txt
python seeds/generate_seed.py --scenario usdt_mica_ban
```

Or connect any MCP client directly:
```bash
npx -y mcp-remote https://mcp.feedoracle.io/mcp
```

**Claude Desktop / Cursor / Windsurf:**
```json
{
  "mcpServers": {
    "feedoracle": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.feedoracle.io/mcp"]
    }
  }
}
```

---

## 🎯 Pre-Built Simulation Scenarios

| # | Scenario | Tools Used | Agents |
|---|----------|------------|--------|
| 1 | **USDT loses MiCA license** | mica_status, peg_deviation, market_liquidity, significant_issuer | 5,000 |
| 2 | **DORA enforcement hits banks** | assess_all, gap_report, incident_report, vendor_risk | 3,000 |
| 3 | **Stablecoin bank run** | peg_history, evidence_bundle, custody_risk, macro_risk | 10,000 |
| 4 | **Fed rate shock on crypto** | macro_risk, fed_rates, yield_data, crypto_prices | 5,000 |
| 5 | **EU bans non-compliant stablecoins** | mica_full_pack, compliance_preflight, evidence_leaderboard | 8,000 |
| 6 | **Carbon credit crash** | carbon_eu_ets_price, carbon_footprint, ESG_scores | 3,000 |
| 7 | **Insurance sector AI adoption** | insurance_tools, DORA_assessment, vendor_risk | 2,000 |
| 8 | **DeFi protocol exploit** | crypto_prices, smart_money, DEX_liquidity, peg_deviations | 7,000 |
| 9 | **Gold-backed stablecoin launch** | metals_gold, metals_silver, reserve_quality, mica_status | 4,000 |
| 10 | **Global recession impact on RWA** | macro_risk, evidence_leaderboard, yield_data, rwa_scores | 6,000 |

---

## 📡 Available Oracle Servers (44)

### 🏛️ Compliance & Regulation (20 Servers, 250+ Tools)

| Oracle | Tools | Domain | Endpoint |
|--------|-------|--------|----------|
| **FeedOracle Core** | 33 | MiCA, DORA, RWA, Macro, ZK Proofs | `mcp.feedoracle.io/mcp` |
| **DORA AmpelOracle** | 24 | DORA assessment, traffic-light | `feedoracle.io/ampel/mcp/` |
| **MiCA Oracle** | 20 | Token/entity MiCA assessment | `feedoracle.io/mica-ampel/mcp/` |
| **DORA Oracle** | 15 | CVE monitoring, ICT incidents | `tooloracle.io/dora/mcp/` |
| **AML Oracle** | 12 | Sanctions, PEP, KYC | `tooloracle.io/aml/mcp/` |
| **Insurance Oracle** | 12 | Solvency II, claims | `tooloracle.io/insurance/mcp/` |
| **Incident Oracle** | 12 | ICT incidents (DORA Art.19) | `tooloracle.io/incident/mcp/` |
| **Crypto Compliance** | 10 | Advanced crypto compliance | `tooloracle.io/crypto2/mcp/` |
| **Contract Oracle** | 10 | ICT contracts (DORA Art.28) | `tooloracle.io/contract/mcp/` |
| **Register Oracle** | 10 | ICT asset registers | `tooloracle.io/register/mcp/` |
| **Policy Oracle** | 10 | ICT security policies | `tooloracle.io/policy/mcp/` |
| **Access Oracle** | 10 | Access management | `tooloracle.io/access/mcp/` |
| **Governance Oracle** | 10 | ICT governance (DORA Art.5) | `tooloracle.io/governance/mcp/` |
| **Change Oracle** | 10 | Change management | `tooloracle.io/change/mcp/` |
| **Resilience Oracle** | 10 | Business continuity | `tooloracle.io/resilience/mcp/` |
| **Dependency Oracle** | 10 | ICT dependencies | `tooloracle.io/dependency/mcp/` |
| **TLPT Oracle** | 10 | Penetration testing (Art.26) | `tooloracle.io/tlpt/mcp/` |
| **Sharing Oracle** | 8 | Threat intelligence sharing | `tooloracle.io/sharing/mcp/` |
| **Training Oracle** | 8 | ICT training & awareness | `tooloracle.io/training/mcp/` |

### 💰 Finance & Markets (8 Servers, 80+ Tools)

| Oracle | Tools | Domain | Endpoint |
|--------|-------|--------|----------|
| **Crypto Oracle** | 12 | BTC/ETH/SOL prices | `tooloracle.io/crypto/mcp/` |
| **Macro Oracle** | 8 | FRED data, Fed rates | `tooloracle.io/macro/mcp/` |
| **Yield Oracle** | 8 | DeFi/RWA yields | `tooloracle.io/yield/mcp/` |
| **SmartMoney** | 8 | Whale tracking | `tooloracle.io/smart/mcp/` |
| **Price Oracle** | 7 | Cross-market prices | `tooloracle.io/price/mcp/` |
| **Invoice Oracle** | 10 | Invoice processing | `tooloracle.io/invoice/mcp/` |
| **Carbon Oracle** | 11 | EU ETS, ESG | `tooloracle.io/carbon/mcp/` |
| **Ecommerce** | 8 | Product data | `tooloracle.io/ecommerce/mcp/` |

### 🌍 Intelligence (8 Servers, 80+ Tools)

| Oracle | Tools | Domain | Endpoint |
|--------|-------|--------|----------|
| **News Oracle** | 9 | Breaking news | `tooloracle.io/news/mcp/` |
| **News Oracle 2** | 8 | Deep analysis | `tooloracle.io/news2/mcp/` |
| **Rank Oracle** | 13 | SEO, SERP | `tooloracle.io/rank/mcp/` |
| **Lead Oracle** | 7 | Prospecting | `tooloracle.io/lead/mcp/` |
| **SEO Oracle** | 7 | On-page SEO | `tooloracle.io/seo2/mcp/` |
| **Review Oracle** | 8 | Product reviews | `tooloracle.io/review/mcp/` |
| **Meme Oracle** | 9 | Meme coins, trends | `tooloracle.io/meme/mcp/` |
| **Shop Oracle** | 11 | E-commerce intel | `tooloracle.io/shop/mcp/` |

### ✈️ Consumer & Lifestyle (7 Servers, 70+ Tools)

| Oracle | Tools | Domain | Endpoint |
|--------|-------|--------|----------|
| **Weather** | 10 | Global weather | `tooloracle.io/weather/mcp/` |
| **Sport** | 12 | Scores, standings | `tooloracle.io/sport/mcp/` |
| **Movie** | 12 | Movie database | `tooloracle.io/movie/mcp/` |
| **Map** | 12 | Geocoding, routing | `tooloracle.io/map/mcp/` |
| **Job** | 8 | Job market | `tooloracle.io/job/mcp/` |
| **Hotel** | 8 | Hotel search | `tooloracle.io/hotel/mcp/` |
| **Flight** | 8 | Flight search | `tooloracle.io/flight/mcp/` |

---

## 🔧 How It Works

```
┌─────────────────────┐     ┌──────────────────────────┐     ┌─────────────────────┐
│  Seed Generator     │     │  44 Oracle Servers        │     │  MiroFish           │
│  (this repo)        │────▶│  484 MCP Tools            │────▶│  Simulation Engine  │
│                     │     │  ECDSA-Signed Evidence    │     │  5,000+ Agents      │
│  generate_seed.py   │     │                          │     │  Prediction Report  │
└─────────────────────┘     └──────────────────────────┘     └─────────────────────┘
```

1. Choose a scenario → 2. Generator calls FeedOracle MCP tools → 3. Structured seed document → 4. MiroFish ingests → 5. Agents simulate → 6. Prediction report

---

## 💰 Pricing

| Package | Price | Units | Best For |
|---------|-------|-------|----------|
| **Welcome** | Free | 500 | Try it — register via `kya_register` |
| **Starter** | €49/mo | 1,100 | Individual researchers |
| **Growth** | €199/mo | 5,500 | Daily simulations |
| **Pro** | €499/mo | 17,000 | Production pipelines |
| **Enterprise** | €1,499/mo | 55,000 | Institutional use |

Annual: 2x bonus + 17% savings. Agents get HTTP 402 with self-service topup.

---

## 🔗 Links

- **Dashboard:** [feedoracle.io/ampel/](https://feedoracle.io/ampel/)
- **Console:** [feedoracle.io/console/](https://feedoracle.io/console/)
- **MCP:** `https://mcp.feedoracle.io/mcp`
- **Whitepaper:** [feedoracle.io/whitepaper.html](https://feedoracle.io/whitepaper.html)
- **MiroFish:** [github.com/666ghj/MiroFish](https://github.com/666ghj/MiroFish)

---

*Built by [FeedOracle](https://feedoracle.io) — Evidence-grade data infrastructure for regulated workflows.*
