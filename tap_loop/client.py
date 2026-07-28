"""HTTP API client for Loop Admin API streams."""

from __future__ import annotations

from typing import Any

import requests
from hotglue_singer_sdk.authenticators import APIKeyAuthenticator
from hotglue_singer_sdk.streams import RESTStream
from typing_extensions import override


class LoopStream(RESTStream):
    """Base Loop Admin API stream."""

    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = None
    page_size = 100
    request_delay_seconds = 0.0
    paginate = True

    @override
    @property
    def url_base(self) -> str:
        return "https://api.loopsubscriptions.com/admin/2023-10"

    @override
    @property
    def authenticator(self) -> APIKeyAuthenticator:
        return APIKeyAuthenticator(
            stream=self,
            key="X-Loop-Token",
            value=self.config["api_key"],
            location="header",
        )

    @override
    @property
    def http_headers(self) -> dict[str, str]:
        return {"Accept": "application/json"}

    @override
    def get_next_page_token(
        self,
        response: requests.Response,
        previous_token: Any | None,
    ) -> Any | None:
        if not self.paginate:
            return None
        if response.json().get("pageInfo", {}).get("hasNextPage"):
            return (previous_token or 1) + 1
        return None

    @override
    def get_url_params(
        self,
        context: dict | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {
            "pageNo": next_page_token or 1,
            "pageSize": self.page_size,
        }
        starting_timestamp = self.get_starting_timestamp(context)
        if self.replication_key and starting_timestamp is not None:
            params["updatedAtStartEpoch"] = int(starting_timestamp.timestamp())
        return params
