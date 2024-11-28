import pandas as pd
import os
import numpy as np

data=pd.DataFrame({
    "name":['Alice','bob','charlie'],
    "age":[25,30,35],
    "city":["New York",'Los Angles',"Chicago"]
})

#path where data will be stored
DATA_DIR='data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DATA_PATH=os.path.join(DATA_DIR,'sample.csv')

#saving csv file
data.to_csv(DATA_PATH,index=False,header=True)

print(f"Saved the CSV file Successfully!")
