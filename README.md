# tap-loop

A [Singer](https://www.singer.io/) tap that extracts data from **Loop Subscriptions** (Loop Admin API). It is built with [hotglue-singer-sdk](https://github.com/hotgluexyz/HotglueSingerSDK) and speaks the standard Singer message protocol on stdout, so you can pair it with any compatible target.

## Features

- **REST** Admin API streams (`client.py`, `streams.py`, `schemas.py`).
- **API key** authentication via `X-Loop-Token` header.
- Page-based pagination (`pageNo` / `pageSize`) with `pageInfo.hasNextPage`.
- Per-stream rate limiting to respect Loop API limits.

### Streams

| Stream | Path | Primary key | Replication key | Rate limit |
| ------ | ---- | ----------- | --------------- | ---------- |
| `subscriptions` | `GET /admin/2023-10/subscription` | `id` | `updatedAt` (via `updatedAtStartEpoch`) | 2 req / 3 sec |
| `customers` | `GET /admin/2023-10/customer` | `id` | full table | 1 req / sec |
| `products` | `GET /admin/2023-10/product?type=ALL` | `shopifyId` | full table | 6 req / sec |

**Token scopes:** subscriptions require *Read subscription contracts*; customers require *Read customers*.

## Requirements

- Python **3.10+** (see `requires-python` in `pyproject.toml`).

## Installation

1. Clone this repository and `cd` into the project directory.
2. Create `.secrets/config.json` with your Loop Admin API token (see [Configuration](#configuration)).
3. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install the package in editable mode:

```bash
pip install -e .
```

5. Verify the CLI:

```bash
tap-loop --help
```

## Configuration

| Setting | Type | Required | Default | Description |
| ------- | ---- | -------- | ------- | ----------- |
| `api_key` | string | yes | — | Loop Admin API token (`X-Loop-Token` header). |
| `start_date` | string (datetime) | no | `2000-01-01T00:00:00Z` | Earliest subscription `updatedAt` to sync. |
| `api_url` | string | no | `https://api.loopsubscriptions.com` | Base URL for the Loop Admin API. |

Run `tap-loop --about` for the authoritative schema for your installed version.

### Example `.secrets/config.json`

```json
{
  "api_key": "YOUR_LOOP_ADMIN_API_TOKEN",
  "start_date": "2000-01-01T00:00:00Z"
}
```

Do not commit real credentials.

## Usage

Discover stream catalog:

```bash
tap-loop --config .secrets/config.json --discover > .secrets/catalog.json
```

Run a sync:

```bash
tap-loop --config .secrets/config.json --catalog .secrets/catalog-selected.json
```

## API documentation

- [Loop Admin API reference](https://developer.loopwork.co/reference)
- [Pagination](https://developer.loopwork.co/reference/pagination)
- [Read all subscriptions](https://developer.loopwork.co/reference/read-all-subscriptions)
- [Read all customers](https://developer.loopwork.co/reference/read-all-customers)
- [List products](https://developer.loopwork.co/reference/list-products)

## License

MIT — see `LICENSE` and `pyproject.toml`.
