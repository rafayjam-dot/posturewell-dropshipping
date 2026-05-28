# SOP: Returns and refunds

PostureWell ships overseas via DSers, so blanket return shipping is rarely worth it. This SOP keeps customers happy without bleeding cash on freight.

## Policy summary (customer-facing)

- 30-day satisfaction guarantee on every order.
- Refunds or replacements available within that window, no return required for items under $25 unit cost.
- For items above $25 unit cost or where a return is requested by the buyer, a prepaid label is issued only after photo evidence is reviewed.

## Decision tree

1. Is the order within 30 days of delivery (or order date if not yet delivered)?
   - No -> follow `sops/customer-service.md` under "Refund request after 30 days".
      - Yes -> continue.
      2. Is the product unit cost above $25?
         - No -> refund or replace without requesting return. Log SKU + supplier for defect tracking.
            - Yes -> request photo evidence; if defective, replace without return; if simply unwanted, issue prepaid label.
            3. Has the buyer already filed a chargeback?
               - Yes -> stop here, follow `sops/customer-service.md` under "Chargeback notification".

               ## Refund mechanics

               - Refund through Shopify Admin so the payout reconciles automatically.
               - Always refund to the original payment method.
               - Restocking fees: never charge them on PostureWell.

               ## Replacements

               - Re-order via DSers using the same supplier from `suppliers/dsers-mapping.md`. Add a note `replacement for #ORDER_NAME` so the supplier flags it for priority shipping.
               - If the same supplier already failed for this customer, switch to the backup supplier.

               ## Tracking & reporting

               - Log every refund and replacement in the monthly ops review with: order, SKU, reason code (`damaged`, `wrong-item`, `lost-in-transit`, `unwanted`), cost impact.
               - Flag any SKU with refund rate above 5 percent over a 30-day rolling window for sourcing review.
               
