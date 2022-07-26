## Leverage-based Pool Ranking Recommendation

Pool ranking scores in wallet browsers have a significant and powerful game theory impact on delegator pool choices, yet it is often overlooked and not transparent in wallets.

When pledge becomes the most important factor for total pool size, lower leverage factors are more desirable. Lists should be sorted by leverage and presented in an ascending order with the lowest leverage pools first.

The following is guidance for what a pool ranking system based on prioritizing pledge leverage should look like at a minimum.

### Ranking Equation

The recommended ranking equation starts with a highest score of 10. The pools are down-ranked soley based on only leverage and fees factors.

    //equation
    ranking_score = 10 - leverage_factor_term - fee_factor_term

    //variables
    leverage_factor_term = 10 * max{ (pool_leverage/L)^A, (pool_stake/saturation_stake)^B }
    fee_factor_term = C * pool_fee_margin

    //parameters
    - A is 2, has range (0,10), can be tweaked
    - B is 2, has range (0,10), can be tweaked
    - pool_leverage = delegation / pledge
    - pool_stake = pledge + delegation
    - saturation_stake = pool_size soft-cap (e.g. 68M Ada based on k-parameter)
    - C is 50, has range (0-100) ish to be harsh, can be tweaked
    - pool_fee_margin is in range (0-100)%

To evaluate rank using the current reward scheme:

    //current reward scheme only
    ranking_score = 10 - leverage_factor_term - fee_factor_term - fixed_fee_factor

    //variables
    //if fee = minFee, term drops out
    //if fee > minFee, term nonzero but loses relevance w/stake
    //fixed fee maters less to rewards as stake grows, so to here
    fixed_fee_factor = D * (fee-minFee) / stake 

    //parameters
    - D is 50, has range (0,100), can be tweaked 

### Ranking System

The pool ranking system will be a descending sorted list of ranking scores, with the highest at the top:

    ranking = sort(ranking_score, order=descending)

The ranking score is intentionally simple and familiar. Pools will be ranked out of a score of 0-10, and "Graded" for ease per below. There can be many pools having the same ranking score.  All wallets should make transparent the knock-down factors that drove the pool's score.

| Grade | Score X/10 |
| --- | --- |
| A | 10-9 |
| B | 8-7 |
| C | 6-5 |
| D | 4-3 |
| F | 2-0 |

### Pool Life-Cycle

A typical pool's life-cycle will emulate a free market of prices based on supply and demand.  Thus, a pool will have a business life-cycle, or choose to sustain healthy operation with moderate fees once established.  This will be healthy free-market dynamics given what stage of life a pool is in, and regulate leverage and fees. Currently, there is market regulation on fees (driving yield), but not leverage.

**Grade A Territory**

1. Start-up: Start with a pledge, low leverage, very low fees, become highly ranked. (Grade A Zone)

2. Customer Aquisiton: Gain delegation, leverage starts to grow, eventually some rewards are gained. Equivalent to a "sale". (Grade A Zone).

**Grade B-C Territory**

3. Sustainment: Raise fees to a moderate, sustainable operating "happy place" level.  Delegators are happy, even though the pool loses some ranking, that is okay. Prices (fees) are sustained by the pool's demand. Pools can sustain operation here indefinitely if desired by modulating pledge leverage and/or fees.

**Grade D-F Territory**

4. Accumulation: High delegation demand and leverage grows.  Raise fees to gain more rewards and grow pledge, higher fees sustained by demand for some time, delegators start to leave, leverage starts dropping back to healthy levels.  High fees can be sustained to force very low leverage (lose delegators) for a higher ranking.

5. Reset: Increases pledge, decrease leverage, increase the pool size, lowers fees, climb back to Grade A Territory.

