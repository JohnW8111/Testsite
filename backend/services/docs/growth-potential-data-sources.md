# Growth potential data sources by sector

This mapping focuses on datasets that can proxy growth potential (revenue/output growth, demand growth, investment/capex, and leading indicators) for the 11-sector taxonomy.

## Common cross-sector sources (use for all 11 sectors)
- **BEA GDP by Industry** (value added growth, real output) — sector-level output growth proxies.
- **BLS Employment & Wages (CES/QCEW)** — employment growth and wage pressure by industry.
- **FRED** (macro leading indicators, industrial production indexes) — sector-linked time series.
- **Census Bureau** (Annual Business Survey, Economic Census) — establishment counts, sales, and growth.
- **SEC EDGAR / company filings** — sector-aggregated revenue and capex growth proxies.

## Sector-specific growth potential sources

## Example build-out: Consumer Discretionary (public data only)
The Consumer Discretionary sector is a practical starting point because it has a wide set of public, high-frequency demand indicators (retail sales, PCE, consumer confidence) and clear leading signals (credit, sentiment, and durable goods orders). Below is a concrete, public-only mapping you can use to compute growth potential signals and a sector score.

### Recommended public datasets
- **Census Monthly Retail Trade (MRTS)** — category-level retail sales (e.g., autos, apparel, e-commerce). Use YoY growth and 3–6 month momentum.
- **BEA Personal Consumption Expenditures (PCE)** — discretionary spending categories (durables, recreation, restaurants). Use real PCE growth for demand.
- **BLS Employment (CES)** — employment and wage growth for retail trade, leisure/hospitality, and relevant discretionary subsectors.
- **Conference Board Consumer Confidence / University of Michigan Sentiment** — forward-looking demand and spending propensity.
- **Federal Reserve G.19 (Consumer Credit)** — revolving credit growth as a proxy for willingness to spend.
- **Census Housing Starts / Building Permits** — indirect signal for housing-related discretionary demand (furnishings, appliances).

### Example growth potential signals (public-only)
- **Demand growth**: YoY % change in discretionary PCE + retail sales (weighted).
- **Momentum**: 3-month annualized growth in retail sales and durable goods categories.
- **Labor tailwind**: YoY employment and wage growth in retail/leisure.
- **Sentiment**: normalized consumer confidence index (z-score vs. 5y average).
- **Credit support**: YoY growth in revolving credit balances.

### Example sector growth score (illustrative weights)
```
GrowthScore_Discretionary =
  0.35 * DemandGrowth +
  0.20 * Momentum +
  0.20 * LaborTailwind +
  0.15 * Sentiment +
  0.10 * CreditSupport
```

This is a starting point; once you have historical outcomes, you can re-weight based on predictive performance.

### 1) Energy
- **EIA (Energy Information Administration)** — energy production/consumption forecasts, capacity additions, price outlooks.
- **FERC** — grid interconnection queues and approvals (renewables buildout).
- **IEA (International Energy Agency)** — global energy demand and investment outlooks.

### 2) Materials
- **USGS Mineral Commodity Summaries** — production volumes and price trends by material.
- **American Chemistry Council** — chemical production statistics.
- **World Bank Commodity Markets (Pink Sheet)** — commodity price and demand outlooks.

### 3) Industrials
- **Census Durable Goods & Manufacturers’ Shipments** — orders and shipments growth.
- **ISM Manufacturing PMI** — forward-looking production/demand index.
- **ATA (trucking) / AAR (rail)** — freight volume trends.

### 4) Consumer Discretionary
- **Census Retail Sales** — category-level retail growth.
- **BEA Personal Consumption Expenditures (PCE)** — discretionary spend growth.
- **Conference Board Consumer Confidence** — leading demand indicator.

### 5) Consumer Staples
- **BEA PCE (non-durables)** — staple consumption growth.
- **USDA** — food price indexes and demand indicators.
- **Nielsen/IRI (commercial)** — category-level sales growth.

### 6) Healthcare
- **CMS National Health Expenditure Accounts** — healthcare spend growth.
- **CDC / NIH** — disease prevalence trends and clinical activity proxies.
- **IQVIA (commercial)** — prescription volume and spend growth.

### 7) Financials
- **FDIC Quarterly Banking Profile** — loan growth, net interest margins.
- **Federal Reserve (H.8, Z.1)** — credit growth and balance sheet trends.
- **SIFMA / FINRA** — capital markets issuance and trading volumes.

### 8) Information Technology
- **BEA / BLS productivity & IT investment** — investment growth in software/hardware.
- **SEMI / WSTS** — semiconductor shipments and sales forecasts.
- **Gartner / IDC (commercial)** — enterprise IT spend growth.

### 9) Communication Services
- **FCC Broadband Deployment** — coverage expansion metrics.
- **CTIA / GSMA** — mobile subscriber growth and 5G adoption.
- **Nielsen / Comscore (commercial)** — media consumption growth.

### 10) Utilities
- **EIA** — electricity demand and generation capacity forecasts.
- **EPA** — emissions standards impact and compliance costs.
- **Regional Transmission Organizations (ISO/RTO)** — load forecasts and capacity additions.

### 11) Real Estate
- **FHFA / Case-Shiller** — price index growth.
- **Census Housing Starts / Building Permits** — leading supply indicators.
- **NMHC / CoStar (commercial)** — vacancy rates and rent growth.
