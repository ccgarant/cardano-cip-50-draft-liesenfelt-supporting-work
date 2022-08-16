## Leverage-based Pool Ranking Recommendation

Pool ranking scores in wallet browsers have a significant and powerful game theory impact on delegator pool choices, yet it is often overlooked and not transparent in wallets.

When pledge becomes the most important factor for total pool size, lower leverage factors are more desirable. Lists should be sorted by leverage and presented in an descending order with the lowest leverage pools first.

### Ranking Equation

The recommended ranking equation starts with the highest score of 10. The pools are down-ranked solely based on leverage, saturation, and fee factors.

    //equation
    ranking_score = 10 - max{ leverage_factor, saturation_factor } - fee_factor

    //variables
    leverage_factor = 10 * (pool_leverage/L)^A
    saturation_factor = 2 * (pool_stake/(saturation_stake * C))^B
    fee_factor = D * pool_fee_margin

    //parameters
    - A is 2.0, has range (0,10.0), can be tweaked
    - B is 5.0, has range (0,10.0), can be tweaked
    - C is 0.9, has range (0,2.0), can be tweaked
    - D is 50, has range (0-100) ish to be harsh, can be tweaked
    - pool_leverage = delegation / pledge
    - pool_stake = pledge + delegation
    - saturation_stake = total_live_stake/k (e.g. 68M₳ "soft-cap upper limit")
    - pool_fee_margin is in range (0-100)% (fixed fee + margin combined)

To evaluate rank using the current reward scheme:

    //current reward scheme only
    ranking_score = 10 - max{ leverage_factor , saturation_factor } - fee_factor - fixed_fee_factor

    //variables
    //if fee = minFee, term drops out
    //if fee > minFee, term nonzero but loses relevance w/ increased stake
    //fixed fee matters less to rewards as stake grows, so too here
    fixed_fee_factor = E * (fee-minFee) / stake 

    //parameters
    - E is 100, has range (0,100_000), can be tweaked
    - fee cannot be less than minFee

#### A Pool's Life-Cycle

A leverage-based ranking system will create interesting pool free market business dynamics. It's envisioned a pool will undergo "business life-cycles" based on price supply and demand (fees) and leverage (pledge raising to grow the business) as described below. Currently, the yield-based pool ranking creates a market based on fees (driving yield), but not leverage, thus pools  can grow indefinitely with no "leverage ranking costs".

_A Leverage-Based Pool's Life-Cycle_
1. Start-up: Low pledge, very low leverage, very low fees, very highly ranked.
2. Growth: Gain delegation, leverage grows, rewards gained, high rank.
3. Sustainment: Raise fees, sustainable operation, moderate ranked.
4. Accumulation: Delegator surplus, high leverage, raise fees, high rewards, low rank.
5. Reset: Lower fees, increase pledge, regain low leverage and high rank. Repeat.

With the need to grow pledge to grow pool size and regain better ranking, the business cycle is cyclical indefinitely until the pool reaches max saturation based on the k-parameter.
