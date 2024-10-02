import pandas as pd
analysis_df=pd.read_json("C:\Users\NGong\OneDrive - Eastside Preparatory School\Documents\IS stuff\SPD_Crime_Data__2008-Present_20240914.csv")
date_time_df=analysis_df.groupby(['Offense Start DateTime','Offense End DateTime','Report DateTime','Offense'])
