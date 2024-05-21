# Pesticide use in California analysis
# 
# https://www.kaggle.com/usgs/pesticide-use
# This dataset includes annual county-level pesticide use estimates for 423 pesticides 
# (active ingredients) applied to agricultural crops grown in the contiguous United States.

import matplot.lib as plt
import numpy as np
import pandas as pd

df_pest_2014 = pd.read_csv("../data/2014.csv")
df_pest_2015 = pd.read_csv("../data/2015.csv")


def analysis():    
    
    print("Pesticide use analysis")


if __name__ == "__main__":
    analysis()
