import numpy as np 
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.measure import label 

coins=np.load("coins.npy.txt")
labeled=label(coins)
def area (labeled, label=1):
    return (labeled [labeled==label]/label).sum()
coin_values = {}
for lb in range(1, np.max(labeled)+1):
    coin_area=area(labeled, lb)
    if coin_area not in coin_values:
        coin_values[coin_area]=1
    else: coin_values[coin_area]+=1
print(coin_values)    
total=0
nominal=[1, 2 , 5, 10]
for i,p in enumerate(sorted(coin_values.items())): 
    total+=nominal[i]*p[1]
print(total)
plt.imshow (coins)
plt.show()