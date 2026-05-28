# posturewell-dropshipping

Operations repository for the **PostureWell** Shopify dropshipping store. This repo tracks the product catalog, supplier mappings (DSers / AliExpress), automation scripts, and the standard operating procedures (SOPs) the store runs on.

## Store at a glance

- **Brand:** PostureWell
- - **Platform:** Shopify
  - - **Niche:** Posture correction & ergonomic wellness (posture correctors, lumbar supports, ergonomic accessories)
    - - **Fulfillment:** Dropshipping via DSers + AliExpress suppliers
      - - **Primary markets:** US, CA, UK, AU
       
        - ## Repository layout
       
        - ```
          posturewell-dropshipping/
            README.md                 <- you are here
            .gitignore
            products/                 <- product catalog & per-product specs
              catalog.csv
            suppliers/                <- supplier mappings, lead times, contacts
              dsers-mapping.md
            sops/                     <- standard operating procedures
              order-fulfillment.md
              customer-service.md
              returns-and-refunds.md
            marketing/                <- ad copy, creative briefs, UTM conventions
              ad-copy-library.md
            automation/               <- helper scripts (Shopify / DSers exports etc.)
              sync_orders.py
              requirements.txt
            docs/                     <- longer-form internal docs
              pricing-strategy.md
          ```

          ## How we work

          1. **Product research** is logged as a draft row in `products/catalog.csv` with status `research`.
          2. 2. Once approved, a per-product spec is added under `products/` and the row is promoted to `live`.
             3. 3. Suppliers are mapped 1:1 with the Shopify variant in `suppliers/dsers-mapping.md` so the DSers binding is reproducible if it ever breaks.
                4. 4. Day-to-day operations follow the playbooks in `sops/`.
                   5. 5. Automation lives under `automation/` and is run locally; secrets are never committed (see `.gitignore`).
                     
                      6. ## Conventions
                     
                      7. - Branch naming: `feature/<short-slug>`, `fix/<short-slug>`, `ops/<short-slug>`.
                         - - Commits: present-tense, scoped (e.g. `products: add lumbar-support-pro spec`).
                           - - No credentials, API keys, customer PII, or payment data in this repo. Ever.
                            
                             - ## Security
                            
                             - If you spot a credential or PII in a commit, open a private issue and rotate the secret immediately. See `.gitignore` for the patterns that are blocked by default.
                             - 
