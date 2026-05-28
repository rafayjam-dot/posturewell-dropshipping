"""Sync recent paid Shopify orders into a local CSV for review.

Purpose:
    Pull unfulfilled, paid orders from Shopify and write a flattened CSV to
        ``data/exports/orders_<YYYYMMDD>.csv``. The CSV is .gitignored on purpose,
            this script is the bridge between Shopify and the DSers Open Orders queue.

            Usage:
                python automation/sync_orders.py --days 3

                Auth:
                    Reads SHOPIFY_STORE and SHOPIFY_ADMIN_TOKEN from the environment.
                        Never commit a real token. See .gitignore.
                        """
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import pathlib
import sys
import urllib.parse
import urllib.request
import json

API_VERSION = "2024-10"


def _require_env(name: str) -> str:
      value = os.environ.get(name)
      if not value:
                sys.exit(f"Missing required env var: {name}")
            return value


def fetch_orders(store: str, token: str, since: dt.datetime) -> list[dict]:
      base = f"https://{store}.myshopify.com/admin/api/{API_VERSION}/orders.json"
    params = {
              "status": "open",
              "financial_status": "paid",
              "fulfillment_status": "unfulfilled",
              "created_at_min": since.isoformat(),
              "limit": 250,
    }
    url = base + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": token})
    with urllib.request.urlopen(req, timeout=30) as resp:
              payload = json.load(resp)
          return payload.get("orders", [])


def flatten(order: dict) -> list[dict]:
      rows = []
    for line in order.get("line_items", []):
              rows.append(
                            {
                                              "order_id": order["id"],
                                              "order_name": order["name"],
                                              "created_at": order["created_at"],
                                              "email": order.get("email", ""),
                                              "sku": line.get("sku", ""),
                                              "title": line.get("title", ""),
                                              "quantity": line.get("quantity", 0),
                                              "price": line.get("price", ""),
                                              "shipping_country": (order.get("shipping_address") or {}).get("country_code", ""),
                            }
              )
          return rows


def main() -> None:
      parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=3, help="Lookback window in days.")
    args = parser.parse_args()

    store = _require_env("SHOPIFY_STORE")
    token = _require_env("SHOPIFY_ADMIN_TOKEN")

    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)
    orders = fetch_orders(store, token, since)

    out_dir = pathlib.Path("data/exports")
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d")
    out_path = out_dir / f"orders_{stamp}.csv"

    rows = [r for o in orders for r in flatten(o)]
    if not rows:
              print("No paid unfulfilled orders in window.")
              return

    with out_path.open("w", newline="", encoding="utf-8") as f:
              writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
              writer.writeheader()
              writer.writerows(rows)
          print(f"Wrote {len(rows)} line items across {len(orders)} orders to {out_path}")


if __name__ == "__main__":
      main()
