# CIP-50 Scratch Pad

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#parameters
k = 500      
alpha = 0.3                   #a0
pledge = 10_000               #pool pledge

#static pool parameters
costs = 340                   #c, pool costs (min 340 per block)
margin = 0                    #[%] pool margin
T_inf = 45*10**8              #45*10^8 total max supply
T = 34*10**8                  #total circulating supply
active_stake = 23*10**8       #percent of circulating supply in active stake pools (some in deap pools, or not staked)
total_stake = T               #circulating supply

#sigma pool delegation saturation
sat_start = 0  
sat_end = 200

#total rewards per epoch, set to 1 for rewards to be a percentage
R = 1

#beta, inverse of k ideal pools for simplicity
beta = 1/k      #[float] (fixed param) inverse of desired number of pools k (k=500, beta = 0.002)

#pool saturation max [float, ada] (fixed param)
#about 68M ada to reach max saturation, which is correct per adapools.org
#checked at epoch 334 total circulating stake is 34 BAda per coinmarketcap (25 April 2022)
#max pool size is the total stake divided by the ideal number of pools k
pool_stake_saturation_max = total_stake*(1/k)

#pool saturation percent range [%] (dynamic param)
#[%]start, stop, in increments. (stop+increment because starts at 0)
increment = 0.1             #[%] increment
sat_start = sat_start/100   #[float] convert from percent to decimal
sat_end = sat_end/100       #[float] convert from percent to decimal

#create saturation percent range
sat_range = np.arange(sat_start,sat_end+increment,increment) #[np_array] e.g. 0, 2.1, 0.1 for 0% to 200% in 10% increments

# pool saturation range in ada
# percent range times max ada for fraction of max pool total stake
sigma_stake_range = sat_range*pool_stake_saturation_max      #[float,ada] frac_ada = % * max_ada

#total stake pool stake relative to total_stake, including pledge lambda
sigma_stake = sigma_stake_range/total_stake      #[%, ada/ada]

#creates beta array of same length of sat_range
beta_array = np.repeat(beta, len(sat_range))     #[float] 

#sigma prime
sigma_p = np.minimum(sigma_stake,beta_array)     #[%] compare two arrays and returns a new array containing the element-wise minima.

#[%] lambda, but can use that word because it's a built in function, so lambdah
lambdah_stake = pledge/total_stake                #[%, ada/ada] pledge amount relative to total stake   

#lambda prime
lambdah_p = np.minimum(lambdah_stake,beta)        #[%] compare two numbers and return the min.

#current rewards formula, broken down into coefficients
A = (R/(1+alpha))
B = (sigma_p + lambdah_p*alpha/beta)
C = (sigma_p - lambdah_p)
D = ((1-sigma_p)/beta)
r = A*(B*((C*D)))

# test print
print(f'\nbeta_array:\n{beta_array}')
print(f'\nsat_range:\n{sat_range}')
print(f'\nsigma_stake_range:\n{sigma_stake_range}')
print(f'\nsigma_stake:\n{sigma_stake}')
print(f'\nsigma_p:\n{sigma_p}')
print(f'\nlambdah_p:\n{lambdah_p}')
print(f'\ncurrent rewards:\n{r}')

#data dictionary dataframe
dataDict = {
    'sat_range':sat_range,
    'sigma_stake_range':sigma_stake_range,
    'sigma_stake':sigma_stake,
    'beta_array':beta_array,
    'sigma_p':sigma_p,
    'r':r
}

#create dataframe
df = pd.DataFrame(dataDict)


#plots
df.plot('sat_range','r',grid='minor',figsize=(12,6),title='current rewards')