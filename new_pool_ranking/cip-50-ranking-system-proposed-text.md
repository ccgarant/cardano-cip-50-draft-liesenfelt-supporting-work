## Leverage-based Pool Ranking Recommendation

Pool ranking scores in wallet browsers have a significant and powerful game theory impact on delegator pool choices, yet it is often overlooked and not transparent in wallets.

When pledge becomes the most important factor for total pool size, lower leverage factors are more desirable. Lists should be sorted by leverage and presented in an descending order with the lowest leverage pools first.

### Ranking Equation

The recommended ranking equation starts with the highest score of 10. The pools are down-ranked solely based on leverage and fee factors.

    //equation
    ranking_score = 10 - leverage_factor_term - fee_factor_term

    //variables
    leverage_factor_term = 10 * max{ (pool_leverage/L)^A, (pool_stake/saturation_stake)^B }
    fee_factor_term = C * pool_fee_margin

    //parameters
    - A is 2.0, has range (0,10.0), can be tweaked
    - B is 2.0, has range (0,10.0), can be tweaked
    - pool_leverage = delegation / pledge
    - pool_stake = pledge + delegation
    - saturation_stake = pool_size soft-cap (e.g., 68M₳ based on k-parameter)
    - C is 50, has range (0-100) ish to be harsh, can be tweaked
    - pool_fee_margin is in range (0-100)% (fixed fee + margin combined)

To evaluate rank using the current reward scheme:

    //current reward scheme only
    ranking_score = 10 - leverage_factor_term - fee_factor_term - fixed_fee_factor

    //variables
    //if fee = minFee, term drops out
    //if fee > minFee, term nonzero but loses relevance w/ increased stake
    //fixed fee matters less to rewards as stake grows, so too here
    fixed_fee_factor = D * (fee-minFee) / stake 

    //parameters
    - D is 50, has range (0,100), can be tweaked
    - fee cannot be less than minFee

### Ranking System

The recommended pool ranking system will be a descending sorted list of ranking scores, with the highest score at the top:

    ranking = sort(ranking_score, order=descending)

The ranking score is intentionally simple and familiar. Pools will be ranked out of a score of 0-10, and "Graded" for ease per below. There can be many pools having the same ranking score.  All wallets should make transparent the knock-down factors that drove the pool's score.

| Grade | Score |
| --- | --- |
| A | 10-9 |
| B | 8-7 |
| C | 6-5 |
| D | 4-3 |
| F | 2-0 |

### A Pool's Life-Cycle

A leverage based ranking system will create interesting pool free market business dynamics. It's envisioned a pool will undergo "business life-cycles" based on price supply and demand (fees) and leverage (pledge raising to grow the business) as described below. Currently, the yield-based pool ranking creates a market based on fees (driving yield), but not leverage.

**Grade A Territory- Growth**

1. Start-up: Start with a pledge "down-payment", very low leverage, very low fees, become highly ranked.

2. Growth: Gain delegation, leverage starts to grow, eventually some rewards are gained. Equivalent to a "sale" to gain delegators and grow.

**Grade B-C Territory - Sustainment**

3. Sustainment: Raise fees to a moderate, sustainable operating "happy place" level.  Delegators are content, even though the pool loses some ranking from leverage, that is okay, rewards are healthy. Prices (fees) are sustained by the pool's demand and community. Pools can sustain operation here indefinitely if desired by modulating pledge leverage and/or fees.

**Grade D-F Territory - Accumulation**

4. Accumulation: Given success and demand brings a surplus of delegators, high leverage grows, rankings fall. A pool will need to raise fees to 1) gain more rewards to grow pledge and 2) drop in rankings more to deter and maybe lose delegators.  Delegators leave, leverage starts dropping back to healthy levels.

5. Reset: With increased rewards (savings) from accumulation/sustainment, a pool can increase pledge to decrease leverage, increase pool size even more, lowers fees, and climb back to Grade A "Growth" Territory. Repeat.

With needing to grow pledge to grow pool size and regain better ranking, the business cycle is cyclical indefinitely, until the pool reaches max saturation based on the k-parameter.
