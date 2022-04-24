# Garant Notes and Comments

## Minor Comments

1. In Motivation Section, third paragraph, I found this sentence slightly confusing, had to reread a few times. Is the Nakamoto Coefficient really just k-effective, because it more clearly represents the real group that can 51% attack? This sentences suggests the NC is half the k-effective?

	IS NOW:
    > "The Nakamoto Coefficient is approximately half of k-effective rounded up to the nearest integer. K-effective provides a higher resolution quantification of network decentralization compared to the Nakamoto Coefficient."

	RECOMMEND: (If I understand it right?)
	> "The Nakamoto Coefficient is k-effective rounded up to the nearest integer. K-effective provides a more realistic Nakamoto Coefficient because it represents the real 51% of grouped entities that can commander the network."

2. In The Proposed Reward Formula Section:

	2.1 Recommend a table below quantifying a0 range and resultant pledge %. Took a few times to read, and curious about the range a0 from 10,000 to 100, and 1.0 to 0.
	> "Instead of a0 ranging from 0.0 to infinity the a0 parameter is intended to range from 10,000.0 down to 1.0. An a0 value of 100.0 would require pools to pledge 1.0% of stake and an a0 of 1.0 would require all pools to be 100.0% pledged."
	
	2.2 In the rewards "r" formula, should alpha be a0 instead?  Also, had to look into what is lambda is again.  Might help the reader to redefine variables.

## Suggestions

3. In Motivation, third paragraph, perhaps provide a good reference or background definition on the Nakamoto Coefficient.  To be perfectly honest, I have heard the term alot but did not know what it meant - I had to google it.  This looks like a good reference to consider adding perhaps: https://cardano.stackexchange.com/questions/4699/what-is-the-nakamoto-coefficient-of-cardano

4. Maybe add section numbers to each...section for easier referencing (Austin Powers joke unintentional :) 

5. In The Current Reward Formula Section:

	5.1. Might be worth defining all variables, equations, and some context for the casual reader audience. E.g. R equation, tau, rho, sigma, alpha, 	lambda left undefined. I had to go back and refresh.  Good reference also might be: https://hydra.iohk.io/job/Cardano/cardano-ledger-	specs/delegationDesignSpec/latest/download-by-type/doc-pdf/delegation_design_spec from
    	Shelley ledger design spec https://github.com/input-output-hk/cardano-ledger
    
    5.2. In markdown you could render equations directly if you wanted. E.g. try (see raw text)
	> $$ y=m*x+b $$

	(Note: well, looks like this doesn't work in github markdown, only jupyter notebooks...)

6. In The Proposed Reward Formula:

	6.1. First sentence, recommend "relative to" in lieu of "based on" to help convey the concept of relative stake limit based on a0, up until saturation.

	IS NOW:
	> "The proposed reward retains the function of k for limiting rewards based on stake but repurposes the a0 parameter for enforcing reward limits based on pledge leverage."

	RECOMMEND:
	> "The proposed reward retains the function of k for limiting rewards based on stake but repurposes the a0 parameter for enforcing reward limits **relative to** pledge leverage."
	
    6.2. Might be a good idea to quantify and expand how much more computationally efficient the equation, might be an underrated huge additional benefit to emphasize? At least on a super high level.
	> "The new equation is computationally simple and purposefully does not use logarithms, exponents, or geometric curves"

7. In Recast of a0, second sentence, recommend "relative to" in lieu of "based on".
	IS NOW:
	> "Pledge leverage establishes a different ‘saturation point’ for each pool based on its pledge."

	RECOMMEND:
	> "Pledge leverage establishes a different ‘saturation point’ for each pool **relative to** its pledge."

## Thoughts
- I like the CIP. 
	- I support it, with understanding of thorough testing and further reflection. At face value, it just makes plain sense it's better.
	- love the fair reward scheme and elegant simplicity.
	- I haven't thought thru the game theory new attack vectors, seems like it would be better with higher more purposful a0 pledge against Sybil.
	- I haven't thought thru the social and ecosystem wide impacts of a hardfork, however it's probably best to do this sooner than later to get it right up front, and have governance dictate the a0 and k parameters down the line.
	- I haven't thought thru the private vs public a0 pledge impacts, however I seem to agree it may incentivise decentralization with a multi-delegation approach, than self run private pools (outsource the work, same high rewards)...
- Definitely agree a0 has negligible effect currently
	- good statement: "The pledge incentive is currently a statistically unnoticed benefit used only by large private stakeholders." agree.
	- love the line a0: The pledge yield booster - great concept.
- Definitely agree k saturation limit in reality is a non-factor, just open up more pools, must assume bad actors.
- Change must come from economic incentive, not altruism, which it does incentivize better rewards across the board.
- Side thought: Open source decentralization ranking score tracker?
	- delegation guide
	- single pools best, what size?
	- multi small biz pools okay
	- multi big company pools bad
	- include multi private big business pools (binance, coinbase)
	- company score (sundaeswap, genius yield, liqwid, newm)...
	- open source audit of pool groups / investigation like journalism
		- "these pools might be run by one entity" fyi
- Love the inclusion of the principles section, and very much agree, great guiding compass.  
- Love the simple yet elegant reward equation.  
	- Simple is better.  
	- I'm pretty fluent in math, and the current reward formula is not the most straight forward for sure. F=ma and E=mc^2 is the way.
	- Also efficiency may be a hidden huge incentive too? Also better sybil attack protection?
- Really like the statement: "Stakeholders know there is no way to game the system for yield, **either individually or collectively with governance**, and pledge is absolutely mandatory".  
	- Sometimes I think that future cardano is at risk from stake holder voting to change the rewards scheme to benefit themselves in the future by a cartel or collusion like the banks in 1913 to form the Federal Reserve.  I guess a hardfork would be easier now without peer-to-peer checking nodes.  Best to get it right now, and make it very hard to change later, like the US Constitution Bill of Rights.  The best aspect of bitcoin is the immutable and predictable monetary policy.  It would behoove Cardano to have a basically permanent monetary reward policy going forward to ensure investor confidence, and immutable decentralization insurance.  This is my main concern in Cardano being an invested stakeholder. 
	- (Is this the correct understanding of concensus: In the future, full nodes peer-to-peer checking can reject blocks if SPO nodes are not updated to the "new reward" software update (hardfork). Or is it stakepools running nodes software version before the peer-to-peer full node checking.  Right now, with no p2p full nodes, I believe it is the stake pool node software version that agree and reach concensus.  In the future, will they be like bitcoin miners, where the nodes have the power to reject mined blocks, if the miner is not on the right software version (still learning). 
	- Either way, the earlier the better to make this change, and hopefully be permanent or very hard to change, for investor protection.
