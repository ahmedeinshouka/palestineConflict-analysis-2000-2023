import pandas as pd
import numpy as np
import scipy as scipy
import matplotlib.pyplot as plt
import seaborn as sns
import  warnings
warnings.filterwarnings("ignore")
df =pd.read_csv(r"D:\palestineConflict\src\fatalities_isr_pse_conflict_2000_to_2023.csv")
print(df.head().to_string())