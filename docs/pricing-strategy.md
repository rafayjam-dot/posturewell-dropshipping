# Pricing strategy

Goal: every live SKU clears at least 65 percent gross margin after ad cost target (MER 2.0). Pricing changes happen on the first of each month unless a supplier raises cost mid-month, in which case prices update the next day.

## Formula

```
shopify_price = max(
    supplier_cost * 5.0,           # margin floor
        competitor_median_price * 0.92 # competitive ceiling
        )
        shopify_price = round_to_psychological_price(shopify_price)
        ```

        `round_to_psychological_price` snaps to the nearest `.99` or `.95` ending.

        ## Bundle pricing

        - Buy 2, save 10 percent.
        - Buy 3, save 15 percent.
        - Bundles never drop below 4x supplier cost on the bundle as a whole.

        ## Shipping

        - Free shipping above $35 order subtotal in US/CA.
        - Flat $4.95 below threshold.
        - No free shipping to AU or UK below $50 (supplier lanes are pricier).

        ## Promotions

        - Max 20 percent storewide discount, twice a year (BFCM, summer reset).
        - Email-only coupons capped at 15 percent.
        - Storewide promos and bundle discounts do not stack; cart picks whichever is better for the customer.

        ## When to raise prices

        If 28-day rolling MER stays above 3.0 for two weeks and add-to-cart rate is above 6 percent, lift the SKU price by one psychological tier and re-measure.
        
