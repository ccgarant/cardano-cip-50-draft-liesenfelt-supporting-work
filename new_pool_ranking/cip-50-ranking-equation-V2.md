# On CIP-50 Leverage-based Pool Ranking System V2

***** **IN WORK DRAFT** *****

The following are notes working from first principles to derive the recommended [CIP-50](https://github.com/michael-liesenfelt/CIPs/blob/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/CIP-Liesenfelt-Shelleys_Voltaire_decentralization_update/README.md) leverage-based stake pool ranking equation and methodology.  The final results will be recommended to CIP-50.  Notes are based on thoughts between Michael Liesenfelt and Christophe Garant.

Author of CIP-50: Michael Liensenfelt | [github](https://github.com/michael-liesenfelt) | [twitter](https://twitter.com/DrLiesenfelt)

Supporting Work: Christophe Garant | [github](https://github.com/ccgarant) | [twitter](https://twitter.com/TheStophe)

Date: July 2022

# Ranking System

Q: Should the ranking be a product of the factors, or an average?
A product of the factors would have a sharp drop off.
An average is more intuitive.  But is there a better way.
After discussing with Liesenfelt.  An easier solution was proposed.
How about 10/10 scale, with A B C D F grades, but just subtract from 10.
Also, performance cannot be done, because it is not known what pools are
assigned blocks, only the pools themselves know with the Ouroboros upgrade.
It was agreed upon to do something like:

    ranking = 10 - leverage_factor_term - fee_factor_term

Where:

    ranking system = sort(10 - pledge_factor_term - fee_factor_term , order=descending )

    pledge_factor_term = 10 * max{(pool_leverage/L)^A , (pool_stake/saturation_stake)^B}

    fee_factor_term = C * pool_fee_margin

    //current reward scheme only
    //if fee=minFee term drops out
    //if fee>minFee, then term loses relevance just like rewards w/ larger ///stake
    fixed_fee_factor = D * (fee-minFee)/stake  
    
    Where:

    - A is 2, has range ( ), can be tweaked
    - B is , has range ( ), can be tweaked
    - C is 50, has range (0-100) ish to be harsh, can be tweaked
    - pool_fee_margin is in range (0-100)%
    - pool leverage = delegation/pledge


Scoring:

| Score 10/10 | Grade |
| --- | --- |
| A | 10-9 |
| B | 8-7 |
| C | 6-5 |
| D | 4-3 |
| F | 2-0 |

**ACTION: Going to rev the ranking equation entirely to Rev 2, keep this for documentation**