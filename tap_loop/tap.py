"""Loop tap class."""

from __future__ import annotations

from hotglue_singer_sdk import Stream, Tap
from hotglue_singer_sdk import typing as th
from typing_extensions import override

from tap_loop.streams import (
    CustomersStream,
    ProductsStream,
    SubscriptionsDetailsStream,
    SubscriptionsStream,
)

STREAM_TYPES = [
    CustomersStream,
    ProductsStream,
    SubscriptionsStream,
    SubscriptionsDetailsStream,
]


class TapLoop(Tap):
    """Singer tap for Loop Subscriptions Admin API."""

    name = "tap-loop"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest subscription updatedAt to sync",
            default="2000-01-01T00:00:00Z",
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="Loop Admin API token (sent as X-Loop-Token header)",
        ),
    ).to_dict()

    @override
    def discover_streams(self) -> list[Stream]:
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapLoop.cli()
