# SOP: Order fulfillment via DSers

Applies to every paid Shopify order on PostureWell. Goal: every paid order is forwarded to a supplier with tracking inside 24 hours.

## Cadence

- Mon-Fri: process orders at 09:00 and 17:00 local time.
- Sat-Sun: process orders once, at 11:00 local time.
- During a sale or ad push, add a 13:00 batch on weekdays.

## Step-by-step

1. Open Shopify Admin and confirm new paid, unfulfilled orders. Flag any order with a risk score of `Medium` or `High` for manual review before pushing to DSers.
2. Open DSers, Open Orders tab. Confirm pending orders match the Shopify count.
3. Run `Map by supplier` to make sure every line item has a bound AliExpress listing. If unbound, see `suppliers/dsers-mapping.md` and re-bind before continuing.
4. Select all eligible orders, click `Order` and pay via the team AliExpress account.
5. Wait for DSers to push tracking back into Shopify (usually under 30 minutes). Verify on a random sample of 3 orders.
6. For any order that fails to place (out of stock, shipping restriction, payment decline), move it to the `Needs attention` view and follow `sops/customer-service.md` for buyer comms.

## Definition of done

- 100 percent of paid, low-risk orders placed at supplier within 24h of payment.
- 100 percent of placed orders have a tracking number in Shopify within 72h.
- Zero orders sitting unfulfilled longer than 5 calendar days without a buyer-facing note.

## Escalation

- Supplier silent for 48h after order placement: switch to the backup supplier listed in `suppliers/dsers-mapping.md` and refund-and-replace if already shipped.
- Tracking shows no movement for 10 days after handover: trigger the `lost-in-transit` template in customer service.
