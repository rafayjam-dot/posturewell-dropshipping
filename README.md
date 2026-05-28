# posturewell-dropshipping

Operations repository for the **PostureWell** Shopify dropshipping store. This repo tracks the product catalog, supplier mappings (DSers / AliExpress), automation scripts, and the standard operating procedures (SOPs) the store runs on.

## Store at a glance

**Brand:** PostureWell
**Platform:** Shopify
**Niche:** Posture correction & ergonomic wellness (posture correctors, lumbar supports, ergonomic accessories)
**Fulfillment:** Dropshipping via DSers + AliExpress suppliers
**Primary markets:** US, CA, UK, AU

## Repository layout

```
posturewell-dropshipping/
  README.md              <- you are here
  .gitignore
  products/              <- product catalog & per-product specs
    catalog.csv
  suppliers/             <- supplier mappings, lead times, contacts
    dsers-mapping.md
  sops/                  <- standard operating procedures
    order-fulfillment.md
    customer-service.md
    returns-and-refunds.md
  marketing/             <- ad copy, creatives, email templates
    ad-copy-library.md
  automation/            <- scripts that automate ops
    sync_orders.py
    requirements.txt
  docs/                  <- internal docs and playbooks
    pricing-strategy.md
```

## How we work

1. New products are sourced in DSers, listed on Shopify, then logged in products/catalog.csv with the supplier mapping recorded in suppliers/dsers-mapping.md.
2. Orders flow Shopify -> DSers -> AliExpress supplier. The day-to-day steps live in sops/order-fulfillment.md.
3. Customer inquiries are handled per sops/customer-service.md and sops/returns-and-refunds.md, using the templates in marketing/.
4. Automation scripts in automation/ are run on a schedule (or ad hoc) to keep order, inventory, and tracking data in sync.

## Conventions

SKUs use the prefix PW- followed by a category code and a 3-digit number (for example PW-PC-001 for a posture corrector).
Prices are stored in USD in products/catalog.csv. Per-market prices live in docs/pricing-strategy.md.
Never commit secrets. API keys, store tokens, supplier credentials, and customer PII must stay out of this repo. Use environment variables (see automation/requirements.txt and the .gitignore).
Markdown files use ATX headings (#, ##, ###) and wrap at a soft limit of ~100 characters.

## Status

This repo is the source of truth for how the PostureWell store is operated. It is intentionally small, opinionated, and kept tidy. If something here is out of date, fix it in a commit rather than working around it.
