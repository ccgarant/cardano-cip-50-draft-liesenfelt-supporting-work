# On CIP-50 Leverage-based Pool Ranking System

The following are notes working from first principles to derive the recommended [CIP-50](https://github.com/michael-liesenfelt/CIPs/blob/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/README.md) leverage-based stake pool ranking equation and methodology.  The final results will be recommended to CIP-50.  Notes are based on thoughts between Michael Liesenfelt and Christophe Garant.

Author of CIP-50: Michael Liensenfelt | [github](https://github.com/michael-liesenfelt) | [twitter](https://twitter.com/DrLiesenfelt)

Supporting Work: Christophe Garant | [github](https://github.com/ccgarant) | [twitter](https://twitter.com/TheStophe)

Date: July 2022


# On Proper Stake Pool Ranking

To complete the CIP-50 Liesenfelt Fair Reward Equation total picture game theory, it was noted thru community comments that the stake pool ranking system should be taken into [consideration](https://github.com/cardano-foundation/CIPs/pull/242#issuecomment-1120710769).  It was a valid point.

Therefore, the following is a walk thru in pursuit of a fair and simple stake pool ranking equation from a decentralization, leverage-based approach.  Stake pools will be referred herein as "pools" for short.

## Principles and Assumptions

The first questions to ask are, what matters? Why? Who is the beneficiary? Good for who? What should be included? Excluded?

The following are the key principles and assumptions for pool ranking:
1. **Decentralization** is the first priority.
2. **Less leverage** is more desirable.
1. Pool Ranking shall be **independent and agnostic to the number of pools**.
1. Pool Ranking shall be **independent of pool yield** because that would automatically knock out smaller pools, early pools, or less filled pools.
1. Pool Ranking shall have **no pool size bias**. Big pools are treated the same as small pools.
1. **Performance** matters for delegators. 

## Key Variables, Parameters, and Definitions

The following are the key variables and parameters for pool ranking per epoch:
- **performance** : number of assigned blocks minted vs dropped
- **leverage** : pool_size / pledge
- **pledge** : pool "down payment"
- **L** : pledge leverage factor parameter
- **pool size** : pledge * leverage factor L
- **fee** : pool flat fee from earned rewards (first cut for SPOs)
- **margin** : pool percent fee from earned rewards, left over from the fee (second cut for SPOs)
- **k-parameter, k** : decentralization parameter, number of desired pools, sets max "soft-cap" on pool

-------
## Ranking Variables
Assume you start with all pools ranking the same.  How do you "up-rank" and "down-rank" pools based on these principles?

### Performance Factor
If all the pools are ranked the same to start, you have to down-rank pools that miss assigned blocks to mint.  At the beginning of every epoch, pools are assigned blocks to mint based on their total stake and a luck factor.

**Conclusion: performance definitely matters.**

<p align="center"><img src="equation1-performance.png" width=300></p>

### Yield Factor
In the current reward equation, pool yield is highest for only high pledge or almost fully saturated pools.  That is, only pools "filled" or "almost filled" (read 90-100% saturated) will have the highest yield.

However, the current "pool size", or saturation, is __*fixed*__ at about 68 million Ada at k=500 (July 2022). It is __*not*__ relative to pledge.

The pool size should not drive ranking because that would put small pools and new comers at a perpetual disadvantage.  It would incentivize private institutions or centralized crowd funding to amount 68M Ada first, rather than start a small pool first and work for delegation.  Small pools will surely die, and put decentralization at a disadvantage.

In the new reward equation proposed in CIP-50, pool size is determined by the pledge times the pledge leverage factor $L$.  Reward yield is relative to the minimum of either the pledge down payment $\lambda$ times $L$ leverage factor, total stake delegation $\sigma$, or pool size $1/k$.

<p align="center"><img src="equation4-newRewardsEq.png" width=300></p>

In the newly proposed reward equation, yes only fully saturated pools will have the highest yield still, __*but*__ that upper pool size limit is relative to pledge (i.e. the upper limit is no longer fixed at a very high amount), making it much more fair.

Also, in the new reward equation, if a pool is filled or over-filled (over saturated), then the SPO can put down more pledge to increase the pool size (increase the saturation upper limit), and thus increase their reward size and eventually maximize yield. (Note: This mechanism in theory will also incentivize pool "groups" or multi-pool operators to just run a single big pool and keep extending their pool size upper limit for more rewards.)

Therefore, yield is a fallout of other of pledge, leverage, external delegation and saturation.  If yeild was purely a metric, only the large full pools would survive, and new early pools would be at a disadvantage, hurting decentralization and biasing new delegators.

**Conclusion: No yield ranking bias** 

So if yeild is not a metric, how to you down-rank the pools as they become more saturated, and at what threshold?

### Leverage Factor
Leverage is a harsh parameter, but necessary.

For example, should one be able to put down $100 and buy a $68,000,000 dollar house? That's a 0.00015% down payment leverage, or 1:680,000 ratio.  That doesn't seem quite right at all.  But that's possible with the current stake pool incentive scheme.

Should pools be up-ranked for higher leverage? Probably not.

<p align="center"><img src="equation2-leverage.png" width=300></p>

That doesn't seem right.  Pools should probably be down-ranked for larger leverage, and rewarded for lower leverage (just like buying a house and the loan rate).

Pool leverage can be defined as the pool size divided by pledge. 

$$ leverage, L = pool_-size / pledge $$
$$ leverage, L = (pledge * L) / pledge $$

The relationship between pool size and pledge is determined by the "pledge leverage factor", or $L$.  

In the new ranking equation, $L$ would be the CIP-50 pledge leverage factor defining the ceiling (if less than pool sie or delegated stake).

So far, **less leverage, better ranking**

<p align="center"><img src="equation2-leverage2.png" width=300></p>

#### Introducing Egalitarian Leverage Factor

Is blanket leverage down-ranking necessarily egalitarian?

Perhaps if a pool can't come up with sufficient Ada to climb the ranks thru more pledge, based on geo-political reasons or other, it may be fairer to not have a general blanket up-rank based on leverage.

Rather, a knock-down factor after your pool passes a certain leverage threshold might be more fair.

If your delegated stake $\sigma$ is less than half of the pledge leverage $\lambda * L$, you should get full credit.  If above 50%, the knock-down factor should apply.

If pools are up-ranked universally only accounting for leverage, or pledge amount, the early pool joiners will always be ranked higher, making it hard to get delegated public stake.

As the pledge leverage factor $L$ decreases over time, this will put a big burden on small pools to come up with much more pledge to compete with bigger pools.

**Egalitarian Pledge Leverage Factor** 

A more egalitarian and equal approach is, down-rank if over-levered after a threshold.  Over 50% for the pledge leverage threshold seems fair.

The Eqalitarian Pledge Leverage Factor (ELF) reward mechanism will incentivize healthy leverage, and thus better sybil attack protection.  Pool ranking incentivised putting down more pledge to increase your pool size, and thus 50% pledge leverage threshold before the ranking knock-down factor applies.

<p align="center"><img src="equation3-egalitarian-leverage-factor-simple.png" width=250></p>

$$ ELF = min\bigg\{1,\frac{L*\lambda*\frac{1}{2}}{\sigma}\bigg\} $$

**Conclusion: When delegation exceed 50% of the pledge leverage threshold, ranking decreases.** 

$$ ranking = performance * min\bigg\{1,\frac{pool_-size*\frac{1}{2}}{delegation}\bigg\} $$

### Fee Factor
A higher fee should down-rank the pool, and instead of a fixed cost fee and margin fee, they should be simplified into one "fee" variable.  

The $fee$ is now from 0 to 100 percent, or (0.00-1.00).

100% pool fee should drop the ranking. 0% pool fees should be the best ranking and a free market choice.  

Sybil attack is protected by the new reward equation and pledge amount, so a zero fee is not an issue for security protection.  Zero pledge will yield zero rewards.  A small pledge will have negligible rewards and low ranking from quickly surpassing the pledge leverage 50% threshold (ELF).

**Less fees, better ranking.**

$$ ranking = performance * (1-fee) * min\bigg\{1,\frac{pool_-size*\frac{1}{2}}{delegation}\bigg\} $$


## Final Equation

A 100% ranked pool would have leverage well under limit, would charge low fees, would make all it's blocks.

$$ ranking = performance * (1-fee) * min\bigg\{1,\frac{pool_-size*\frac{1}{2}}{delegation}\bigg\} $$

A pool's cyclical life-cycle of obtaining higher rank will follow:
1. set low fees and establish better ranking, ensure performance is top-notch
2. climb the rankings, gain stake and delegators, approach the pledge leverage 50% threshold
3. raise fees to accumulate more rewards to grow pledge and raise pool size to avoid levered knock-down factor
4. fall in rankings, collect more ada, sustain slow lose of delegators
5. raise the pledge, increase pool size, improve the leverage factor in anticipation of the next growth cycle
6. lower fees, climb rankings, get back to a good ranking (step #1)
7. repeat

## The Ranking System
Instead of a ranking system in numerical ascending order (e.g. 1,2,3,...n), it is proposed to have a normalized, equal size categorical ranking system akin to academic grade scales (e.g. A+, A, A-, B+, B, B-, C+,...F).  This will break up the pools into different performing categories or "buckets" of equal sizing (or should it be a bell-curve?).  There can be many pools with an A+ 100% grade, not just one.  It is then up to the delegator to decide the pool's goods and services in the A+ category or yeild to choose a pool.

The concept is, at the end of each epoch, normalize the ranking for each factor category. That is, for each pool and each category, divide the category factor by the best performing "max" value.  This will normalize all results.  (E.g. if the top test grade is a 60, this then becomes the "best" A+ grade.)

**School Grading System** 

| Letter Grade | Score | Rank |
| --- | --- | --- |
| A+ | 100-97% | 4.0 |
| A   | 93–96%	| 3.9 |
| A− | 90–92%	| 3.7 |
| B+ | 87–89% | 3.3 |
| B | 83–86% |	3.0 |
| B− | 80–82% | 2.7| 
| C+ | 77–79% | 2.3 |
| C | 73–76% | 2.0 |
| C− | 70–72% | 1.7 |
| D+ | 67–69% | 1.3 |
| D | 63–66% | 1.0 |
| D− | 60–62% | 0.7 |
| F | 0–59% | 0.0 |
--- 

This strategy should make it easier for multiple pools to earn 100% A+ score.

To help promote categories, there should be a round up feature for to be determined amount.

$$ ranking = round_-up \bigg[performance * (1-fee) * min\bigg\{\frac{a0}{(2*leverage)},1.0 \bigg\} \bigg]$$

**Ranking Categories**
- performance
- leverage
- fee

**Parameters** 
- L


### Transparency
Pools should be able to see their score for each category.

Pools should be able to see a numerical category ranking to quickly tell where they need improvement, or for the delegator to judge if the down-ranking hit is a concern to them, to make the human action decision themselves.

**Ranking System**

The overall ranking system shall be the average of the individual category ranks.

| Category | Score |
| --- | --- |
| Overall Score | B+ (3.2) |
| Performance | A (3.9) |
| Leverage | B- (2.7) |
| Fees | B (3.0) | 


## Additional Considerations

**Multi pool operator down-ranking?** 

How to determine mathematically a pool "group", or a group of a multi stake pools run by the same operator or entity?  Should these pools be down-ranked?

This is most likely only able to be determined by human judgement, and most likely optionally implemented by the service provided. (e.g. eternl down-ranks multipool operators).  

The community will have to "hivemind" flagging multi pool operators.  This should be open source and subject to rebuttals.

**Pledge not met** 

Warning or down-ranking if pledge not met? Not show the pool at all?

**Weighted equation?** 

Does certain ranking categories carry more weight.  For example, in trade studies, certain criteria carry more weight.

**Delisting**
What should inhibit listing the stake pools?
- If pledge is not met?
- Inactive?

## Summary

The following is the bare minimum new reward stake pool ranking system.

$$ ranking = round_-up \bigg[performance * (1-fee) * min\bigg\{\frac{a0}{(2*leverage)},1.0 \bigg\} \bigg]$$

That takes into account the following categories

**Ranking Categories**
- performance
- leverage
- fee

**Parameters** 
- L

Further knock-down or delisting factors will be up to the service provider to provide as additional radio switches to implement at the delegators discretion.  It is advised to implement the following additional categories in a weighted factor function [Ref 2,3].

Additional Considerations:
- pledge not met
- inactive
- multipool
- yield

$$ new_-ranking = a1 * a2 * a3 * ranking $$

---------------

Ref: 
1. [Suggestions for improvement #19 ccvault github issue tracker](https://github.com/ccwalletio/tracker/issues/19)
2. [Acqnotes, NAS System Engineering Manual, Trade Studies](https://www.acqnotes.com/Attachments/NAS%20SYSTEM%20ENGINEERING%20MANUAL.pdf)
3. [Chapter 4: System Engineering Tools](https://www.eng.auburn.edu/~dbeale/ESMDCourse/Chapter4.htm)

--------------
