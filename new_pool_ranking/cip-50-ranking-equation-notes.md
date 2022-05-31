# CIP-50 Recommended Stake Pool Ranking System

The recommended [CIP-50](https://github.com/michael-liesenfelt/CIPs/blob/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/README.md) stake pool ranking equation, system, and ethos.  

The following are notes working from first principles to derive the recommended CIP-50 stake pool ranking system.  The final results will be added to CIP-50.  Notes are based on thoughts between Michael and Christophe.

Author of CIP-50: Michael Liensenfelt | [github](https://github.com/michael-liesenfelt) | [twitter](https://twitter.com/DrLiesenfelt)

Contribution: Christophe Garant | [github](https://github.com/ccgarant) | [twitter](https://twitter.com/TheStophe)

Date: May 2022


# On Proper Stake Pool Ranking

To complete the CIP-50 Fair Reward Equation Schema, it was noted that to complete the total game theory of the rewards, the stake pool ranking would have to be taken into consideration.

Without proper stake pool ranking, it would be up in the air of how to choose a stake pool in the new CIP-50 reward schema.

Therefore, What is the simplest fair equation for pool ranking?

Leverage * Performance?

What matters? Why? Who is the beneficiary? Good for who?


## Key Variables and Parameters:
- **performance** : number of assigned blocks minted vs dropped
- **leverage** : pool_size / pledge
- **pledge** : stake pool "down payment"
- **fee** : stake pool flat fee from reward for each epoch
- **margin** : stake pool percent fee from rewards per epoch, left over from fee
- **a0** : pledge leverage factor parameter
- **k** : decentralization parameter, number of desired pools


## Principles and Assumptions:
- Should be independent and agnostic to the number of pools or desired k number of pools decentralization parameter.
- Should be independent of yeild because that would automatically knock out smaller pools or less filled pools.
- No size bias (big pool vs small pool). So, no yeild.


# Ranking Variables

### Performance
If all the pools are ranked the same to start, you have to down rank pools that don't make assigned blocks.  

**Performance definitely matters.**

$$ ranking = performance $$

### Yield
Not yield, because that would put small pools at a disadvantage (only high pledge or almost fully saturated pools have the highest yeild).  In the new reward equation, yeild is relative to pledge down payment and delegation, but still, only fully saturated pools will have the highest yeild. Also currently, only 

Yeild is almost a fallout of other variables and parameters.

**No size bias, thus yeild** 


### Leverage
Leverage is a harsh parameter, but necessary.  

$$ leverage = pool_-size / pledge $$

a0 would be the CIP-50 pledge leverage factor defining the ceiling.

That equation basically says, if you are less than half of the a0 pledge leverage factor, you get full credit.  Anymore and it starts dragging your score down.

**Less leverage, better ranking.** 

$$ ranking = performance * (1 / leverage) $$

**Leverage** - equation basically says, if you are less than half of the a0 pledge leverage factor, you get full credit.  Any more and it starts dragging down your score.

### Fee
A higher fee should count against the pool.  Basically less shared rewards fixed amount.  100% pool fee should drop the ranking.

**Less fees, better ranking.**

$$ ranking = performance / leverage * (1-fee) $$


### Margin

## Final Equation

A 100% pool would have leverage well under limit, would charge low or 0 fee, would make all it's blocks.

$$ ranking = performance * (1-fee) * min\bigg\{\frac{a0}{(2*leverage)},1.0\bigg\} $$

## Ranking System
Levels of ranking.  Multiple pools in a ranking level. A scoring system akin to academic grade scales (e.g. A+, A, A-, B+, B, B-, C+ ... etc., or 100...90...80...0).  Could be a bell curve shape.

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

Should make it easy(ier) for a ton of pools to earn 100% score.

Round up floating rank numbers.

$$ ranking = round_up [ performance / leverage * (1-fee) ] $$

**Ranking Categories**
- performance
- leverage
- fees
- margin

**Parameters** 
- a0

**Ranking System**
| Category | Good Ranking Incentive | Bad Ranking Disincentive | 
| --- | --- | ---|
| performance | -- | -- |
| leverage | -- | -- |
| fees | low fees good | high fees bad |
| margin | -- | -- |


### Transparency
Pool should be able to see their score for each category.

Pool should be able to see basically a stop light of colors for their ranking to quickly tell where they need improvement, or the delegator to judge if the deranking hit is a concern to them, to make the decision themselves.

 **Categories**
Ranking per category
dark green, light green, yellow, orange, red
4, 3, 2, 1, 0

or

green, yellow, red
2,1,0


## Additional Considerations

**multi pool operator deranking?** 
How to tell the group? Most likely a ranking system that should be done by a person, not the protocol. (e.g. ccvault deranks multipool operators).

**pledge not met** 
Warning or deranking if pledge not met?

**weighted equation?** 
Does certain ranking categories carry more weight.  For example, in trade studies, certain criteria carry more weight.

### Delisting
What should inhibit listing the stake pools?
- if pledge is not met?
- inactive?

------

Ref: 
1. [Suggestions for improvement #19 ccvault github issue tracker](https://github.com/ccwalletio/tracker/issues/19)
1. [Acqnotes, NAS System Engineering Manual, Trade Studies](https://www.acqnotes.com/Attachments/NAS%20SYSTEM%20ENGINEERING%20MANUAL.pdf)
1. [Chapter 4: System Engineering Tools](https://www.eng.auburn.edu/~dbeale/ESMDCourse/Chapter4.htm)

--------------












