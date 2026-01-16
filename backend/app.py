from __future__ import annotations

import os
from datetime import date
from typing import Dict, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.fred import FREDClient, SeriesPoint


class GrowthSignal(BaseModel):
    name: str
    value: float
    unit: str
    as_of: date
    source: str


class GrowthScoreResponse(BaseModel):
    sector: str
    score: float
    signals: List[GrowthSignal]
    weights: Dict[str, float]


app = FastAPI(title="Sector Growth Potential API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def _normalize_latest(points: List[SeriesPoint]) -> float:
    if len(points) < 2:
        return 0.0
    latest = points[-1].value
    prior = points[-2].value
    if prior == 0:
        return 0.0
    return (latest - prior) / abs(prior)


@app.get("/api/growth/consumer-discretionary", response_model=GrowthScoreResponse)
async def consumer_discretionary_growth() -> GrowthScoreResponse:
    """Compute a simple growth score using public FRED series as proxies.

    Requires FRED_API_KEY env var.
    """

    client = FREDClient(api_key=os.getenv("FRED_API_KEY", ""))

    # Example FRED series:
    # - Retail Sales: Retail and Food Services (RSAFS)
    # - PCE Durable Goods (PCEDG)
    # - Consumer Sentiment (UMCSENT)
    # - Consumer Credit Revolving (REVOLSL)
    series_map = {
        "retail_sales": "RSAFS",
        "pce_durables": "PCEDG",
        "sentiment": "UMCSENT",
        "revolving_credit": "REVOLSL",
    }

    signals: List[GrowthSignal] = []
    signal_values: Dict[str, float] = {}

    for name, series_id in series_map.items():
        points = client.get_series(series_id)
        if not points:
            continue
        growth = _normalize_latest(points)
        signal_values[name] = growth
        signals.append(
            GrowthSignal(
                name=name,
                value=growth,
                unit="rate",
                as_of=points[-1].date,
                source=f"FRED:{series_id}",
            )
        )

    weights = {
        "retail_sales": 0.35,
        "pce_durables": 0.25,
        "sentiment": 0.20,
        "revolving_credit": 0.20,
    }

    score = sum(signal_values.get(key, 0.0) * weight for key, weight in weights.items())

    return GrowthScoreResponse(
        sector="Consumer Discretionary",
        score=score,
        signals=signals,
        weights=weights,
    )
