from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import List

import requests


@dataclass
class SeriesPoint:
    date: datetime.date
    value: float


class FREDClient:
    base_url = "https://api.stlouisfed.org/fred"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_series(self, series_id: str, limit: int = 2) -> List[SeriesPoint]:
        if not self.api_key:
            return []

        response = requests.get(
            f"{self.base_url}/series/observations",
            params={
                "series_id": series_id,
                "api_key": self.api_key,
                "file_type": "json",
                "sort_order": "desc",
                "limit": limit,
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        observations = data.get("observations", [])
        points: List[SeriesPoint] = []
        for obs in observations:
            try:
                value = float(obs["value"])
            except ValueError:
                continue
            points.append(
                SeriesPoint(
                    date=datetime.date.fromisoformat(obs["date"]),
                    value=value,
                )
            )
        return list(reversed(points))
