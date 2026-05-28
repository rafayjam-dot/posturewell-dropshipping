# DSers / AliExpress supplier mapping

Source of truth for which AliExpress supplier is bound to each Shopify variant in DSers. If a DSers binding breaks, re-bind from here.

## Mapping table

| SKU | Shopify variant | DSers status | AliExpress supplier (alias) | Unit cost (USD) | Ship to US (days) | Notes |
|---|---|---|---|---|---|---|
| PW-PC-001 | Classic Posture Corrector / S | bound | supplier-A | 4.10 | 9-15 | Primary |
| PW-PC-001 | Classic Posture Corrector / M | bound | supplier-A | 4.20 | 9-15 | Primary |
| PW-PC-001 | Classic Posture Corrector / L | bound | supplier-A | 4.30 | 9-15 | Primary |
| PW-PC-002 | Pro Posture Corrector (Adjustable) | bound | supplier-B | 6.80 | 9-15 | |
| PW-LS-001 | Mesh Lumbar Support | bound | supplier-C | 5.10 | 10-18 | |
| PW-LS-002 | Memory Foam Lumbar Cushion | bound | supplier-D | 7.50 | 12-20 | Higher AOV |
| PW-NC-001 | Cervical Neck Pillow | bound | supplier-E | 4.90 | 10-16 | |
| PW-ST-001 | Posture Seat Cushion | unbound | supplier-F (candidate) | 3.80 | 10-18 | Pending validation |
| PW-AC-001 | Posture Resistance Band Set | unbound | supplier-G (candidate) | 2.40 | 9-14 | Cross-sell candidate |

## Re-binding playbook

1. In DSers open the variant under Import List or My Products.
2. Find the AliExpress listing for the supplier alias from this file.
3. Confirm the variant SKU and unit cost match (within 10 percent).
4. Bind the variant and place a test order in sandbox mode.
5. Update the DSers status column here and commit.

## Risk flags

- Replace any supplier with more than 2 percent defect rate over the last 100 orders.
- Replace any supplier whose ship-to-US lead time is above 21 days for two consecutive weeks.
- Never bind a supplier without a tracked shipping line (ePacket, Cainiao, or equivalent).
