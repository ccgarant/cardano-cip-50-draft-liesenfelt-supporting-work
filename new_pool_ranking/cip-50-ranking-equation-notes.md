# CIP-50 Recommended Stake Pool Ranking Equation

The recommended [CIP-50](https://github.com/michael-liesenfelt/CIPs/blob/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/README.md) stake pool ranking equation, system, and ethos.  

The following are notes working from first principles to derive the recommended CIP-50 stake pool ranking equation.  The final results will be added to CIP-50.  Notes are based on thoughts between Michael Liesenfelt and Christophe Garant.

Author of CIP-50: Michael Liensenfelt | [github](https://github.com/michael-liesenfelt) | [twitter](https://twitter.com/DrLiesenfelt)

Supporting Work: Christophe Garant | [github](https://github.com/ccgarant) | [twitter](https://twitter.com/TheStophe)

Date: June 2022


# On Proper Stake Pool Ranking

To complete the CIP-50 Liesenfelt Fair Reward Equation total picture game theory, it was noted thru community comments that the stake pool ranking system would have to be taken into consideration.  It was a valid point.

Therefore, the following is a walk thru in pursuit of a fair and simple stake pool ranking equation.  Stake pools will be referred herein as "pools" for short.


## Principles and Assumptions:
The first questions to ask are, what matters? Why? Who is the beneficiary? Good for who?  What should be included? Excluded?

The following are the key principles and assumptions for pool ranking:
1. **Decentralization** is the first priority.
1. Pool Ranking shall be **independent and agnostic to the number of pools** or desired k number of pools decentralization parameter.
1. Pool Ranking shall be **independent of yield** because that would automatically knock out smaller pools or less filled pools.
1. Pool Ranking shall have **no pool size bias** (i.e. saturation size based off pledge) Big pools are treated the same as pools.


## Key Variables and Parameters:

The following are the key variables and parameters for pool ranking per epoch:
- **performance** : number of assigned blocks minted vs dropped
- **leverage** : pool_size / pledge
- **pledge** : pool "down payment"
- **fee** : pool flat fee from earned rewards (first cut for SPOs)
- **margin** : pool percent fee from earned rewards, left over from the fee (second cut for SPOs)
- **a0** : pledge leverage factor parameter
- **k** : decentralization parameter, number of desired pools

-------
## Ranking Variables
Assume you start with many pools of the same ranking.  How do you "up-rank" and "down-rank" pools?

### Performance
If all the pools are ranked the same to start, you have to down-rank pools that miss assigned blocks to mint.  At the beginning of every epoch, pools are assigned blocks to mint based on their total stake and a luck factor.  

**Conclusion: performance definitely matters.**

$$ ranking = performance $$

### Yield
In the current reward equation, pool yield is highest for only high pledge or almost fully saturated pools.  That is, only pools "filled" or "almost filled" (read saturated) will have the highest yield.  

However, the current "pool size", or saturation, is __*fixed*__ at about 68 million Ada at k=500 (June 2022). It is __*not*__ relative to pledge.

The pool size should not drive ranking because that would put small pools and new comers at a perpetual disadvantage.  It would incentivize private institutions or centralized crowd funding amounts of Ada.  Small pools will surely die, and put decentralization at a disadvantage. 

In the new reward equation, pool reward yield is relative to the minimum of pledge down payment $\lambda$ times $a0$ leverage factor, total stake delegation $\sigma$, and pool size $1/k$. 

So yes, only fully saturated pools will have the highest yield still, __*but*__ that upper pool size limit is relative to pledge (i.e. the upper limit is no longer fixed at a very high amount).

Also, in the new reward equation, if a pool is filled or over-filled (over saturated), then the SPO can put down more pledge to increase the pool size (increase the saturation upper limit), and thus increase their reward size and maximize yield. (Note: This mechanism will also incentivize pool "group" or multi-pool operators to just run a single pool can keep extending the upper limit.)

Therefore, yield is a fallout of other of other variables and parameters.

**Conclusion: No size bias, thus no yield ranking bias** 


### Leverage
Leverage is a harsh parameter, but necessary.  

For example, should one be able to put down $100 and buy a $68,000,000 dollar house? That's a 0.00015% down payment.  That doesn't seem quite right.

Should pools be up-ranked for higher leverage?

$$ranking = leverage * performance?$$

That doesn't seem right.  Pools should probably be down-ranked for larger leverage, and rewarded for lower leverage (just like buying a house and the loan rate).

Pool leverage can be defined as the pool size divided by pledge. 

$$ leverage = pool_-size / pledge $$

The relationship between pool size and pledge is determined by the "pledge leverage factor", or $a0$.  

In the new ranking equation, $a0$ would be the CIP-50 pledge leverage factor defining the ceiling (if less than pool sie or delegated stake).

So far, **less leverage, better ranking**

$$ ranking = performance * (1 / leverage) $$

#### Egalitarian Leverage

Is blanket leverage down-ranking necessarily egalitarian?

Perhaps if a pool can't come up with sufficient Ada to climb the ranks thru more pledge, and thus less leverage, based on geo-political reasons or other, it may be fairer to not have a general blanket up-rank based on leverage.

Rather, a knock-down factor after your pool passes a certain leverage threshold might be fairer.

If your stake is less than half of the a0 pledge leverage factor, you should get full credit.  If you Any more and it starts dragging down your score.

If pools are up-ranked universally only accounting for leverage, or pledge amount, the early pool joiners will always be ranked higher.  

As the pledge leverage factor $a0$ decreases over time, this will put a big burden on small pools to come up with much more pledge to compete with bigger pools.

**Leverage knock-down factor** 

A more egalitarian and equal approach is, down-rank if over levered after a threshold.  Over 50% for the pledge leverage threshold seems fair.

What this means is, if your pool leverage (based on pledge) is less than half of the $a0$ pledge leverage factor, you get full credit.  This rewards those who keep healthy pool leverage in check with the parameter $a0$ as the chain evolves.

If your leverage is over half of the pledge leverage factor, it starts dragging down your rank score, applying a knock-down factor.

This reward mechanism will keep pools keeping healthy leverage in line with the protocol evolution.  If your pool stake grows, your pool will become more levered.  To decrease the pool's leverage, more pledge is required. This will be a nice checks-and-balance in line with the pledge leverage factor $a0$ and support chain protocol evolution.

**Conclusion: More pool leverage over 50% of threshold, worse ranking.** 

$$ ranking = performance * min\bigg\{\frac{a0}{(2*leverage)},1.0\bigg\} $$

Note: the min of 1 in the leverage portion is to protect from divide by zero impacts, and put in a nice, even lower limit.


### Fee
A higher fee should down-rank the pool, and instead of a fixed cost fee and margin fee, they should be simplified into one "fee" variable.  

The $fee$ is now from 0 to 100 percent, or (0.00-1.00).

100% pool fee should drop the ranking. 0% pool fees should be the best ranking and a free market choice.  

Sybil attack is protected by the new reward equation and pledge amount.  Zero pledge will yield zero rewards.  A small pledge will have negligible rewards and low ranking.

The fee mechanism will work by a pool performing the following:
1. set low fees and establish better ranking
2. gain stake and delegators, approach pledge leverage 50% threshold
3. raise fees to accumulate more pledge to raise their pool size, avoid levered knock-down factor
4. collect more ada, sustain of lose delegators 
5. raise pledge and thus raise pool size, improve the leverage factor
6. lower fees, get back to good ranking
7. repeat

**Less fees, better ranking.**

$$ ranking = performance * (1-fee) * min\bigg\{\frac{a0}{(2*leverage)},1.0\bigg\} $$


## Final Equation

A 100% ranked pool would have leverage well under limit, would charge low fees, would make all it's blocks.

$$ ranking = performance * (1-fee) * min\bigg\{\frac{a0}{(2*leverage)},1.0\bigg\} $$

## The Ranking System
Instead of a ranking system in numerical ascending order (e.g. 1,2,3,...n), it is proposed to have a categorical ranking system akin to academic grade scales (e.g. A+, A, A-, B+, B, B-, C+,...F).  This will most likely be a bell shaped curve, however, the number of pools that can be ranked A+ is unlimited (or should there be a fixed limit?).  There can be many pools with an A+ 100% grade.  It is then up to the delegator to decide the goods and services as well as yield to choose a pool.

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
- a0


### Transparency
Pools should be able to see their score for each category.

Pools should be able to see a numerical category ranking to quickly tell where they need improvement, or the delegator to judge if the down-ranking hit is a concern to them, to make the decision themselves.

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
- a0

Further knock-down or delisting factors will be up to the service provider to provide as additional radio switches to implement at the delegators discretion.  It is advised to implement the following additional categories in a weighted factor function [Ref 2,3].

Additional Considerations:
- pledge not met
- inactive
- multipool
- yield

$$ new_-ranking = a_1*a_2*a_3*ranking $$

---------------

Ref: 
1. [Suggestions for improvement #19 ccvault github issue tracker](https://github.com/ccwalletio/tracker/issues/19)
2. [Acqnotes, NAS System Engineering Manual, Trade Studies](https://www.acqnotes.com/Attachments/NAS%20SYSTEM%20ENGINEERING%20MANUAL.pdf)
3. [Chapter 4: System Engineering Tools](https://www.eng.auburn.edu/~dbeale/ESMDCourse/Chapter4.htm)

--------------












