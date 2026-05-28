# Ad copy library

Approved copy blocks for PostureWell ads and lifecycle email. Keep entries short, swappable, and tagged with the SKU they back so we never run ads pointing at unbound or out-of-stock variants.

## UTM convention

All paid traffic uses the following query parameters so we can attribute revenue in Shopify Analytics:

- `utm_source`: ad platform (`meta`, `tiktok`, `google`).
- `utm_medium`: `paid_social` or `paid_search`.
- `utm_campaign`: campaign name in kebab-case (e.g. `lumbar-mesh-spring`).
- `utm_content`: creative slug (e.g. `ugc-jen-v3`).
- `utm_term`: ad-set or keyword slug.

## Headlines

| SKU | Hook | Headline | Notes |
|---|---|---|---|
| PW-PC-001 | Pain | "Stop slouching by Friday." | Use with before/after creative |
| PW-PC-001 | Outcome | "The 5-minute posture reset." | Evergreen |
| PW-PC-002 | Authority | "Built for desk jobs that wreck your back." | Office worker angle |
| PW-LS-001 | Comfort | "Your office chair, finally bearable." | Mesh angle |
| PW-LS-002 | Premium | "Memory foam where you actually need it." | Pair with premium creative |
| PW-NC-001 | Sleep | "Wake up without the neck crick." | Night-time angle |

## Body copy blocks

### PW-PC-001 - Classic Posture Corrector

Stop fighting your shoulders. The Classic Posture Corrector gently pulls them back into place, so standing up straight stops being a thing you have to remember. Adjustable for sizes S through L, breathable enough to wear under a shirt.

### PW-LS-002 - Memory Foam Lumbar Cushion

Most lumbar pillows squish flat after a week. This one keeps its shape because the core is memory foam, not bargain-bin fiber fill. Straps fit any office or car seat.

## Customer service templates

### Where is my order (delayed)

> Hi {first_name}, thanks for checking in. Your order #{order_name} is currently in transit and was last scanned in {city} on {date}. Expected delivery is {window}. I will personally follow up if there is no new scan by {date+5d}. Thanks for being patient with us.

### Damaged item replacement

> Hi {first_name}, that is not what we want you to receive. A free replacement is on the way, you will get tracking within 48 hours. Keep the original, no need to return it. Sorry for the trouble.

### Refund confirmation

> Hi {first_name}, your refund of {amount} has been issued back to your original payment method. It usually shows up in 3-5 business days. Let me know if anything else looks off.
