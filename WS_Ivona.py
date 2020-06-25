# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:19:06 2020

@author: USER
"""

import numpy as np
import pandas as pd

df = pd.read_csv('amazon.csv', encoding='ISO-8859-1') 

print(df.head())
print(df.tail())
print(df.shape)

#all columns to lowercase
df.columns = [col.lower() for col in df]
print(df.head())

#check for any missing values
print(df.isnull().sum())
df.dropna(inplace = True)

#round all of the fires number to integers
#df['number'] = round(df['number'], 0)
#df['number'] = np.round(df['number'],0)
df['number'] = pd.to_numeric(df['number'], downcast = 'integer')
print(df.info())

#Ex1, total number of fires in the Acre state
acre_state = (df['state'] == 'Acre').sum()
acre = pd.DataFrame()
acre = df.groupby(['state'])['number'].sum()
acre_fires = acre['Acre']
print(acre_fires)
    
#average number of fires per year
df_temp = df[df['year']<2006]
m = df_temp.groupby(['year'])['number'].sum()
m = np.mean(m)
print(m)

#Ex 2
# total amount of fires in the month of January
df_jan = df[df['month'] == 'Janeiro']
df_jan = df_jan.groupby(['month'])['number'].sum()

#average number of fires per year across all years
mean_year = df.groupby(['year'])['number'].sum()
mean_year = mean_year.mean()
print(mean_year)

#year in which there were the most number of fires in August
df_aug = df[df['month'] == 'Agosto']
df_a = df_aug.groupby('year').agg({'number':'max'}).reset_index()
print(df_a[df_a['number'] == df_a['number'].max()]['year'])

#Ex 3
#number of fires per year
#mean, median and standard deviation
df_stat = df.groupby(['year'])['number']
mean_df = df.groupby(['year'])['number'].sum()
mean_df = mean_df.mean()
print(mean_df)

median_df = df.groupby(['year'])['number'].sum()
median_df = np.median(median_df)
print(median_df)

std_df = df.groupby(['year'])['number'].sum()
std_df = np.std(std_df)
print(std_df)

#number of fires per state
#mean, median and standard deviation
df_stat = df.groupby(['state'])['number']
mean_df = df.groupby(['state'])['number'].sum()
mean_df = mean_df.mean()
print(mean_df)

median_df = df.groupby(['state'])['number'].sum()
median_df = np.median(median_df)
print(median_df)

std_df = df.groupby(['state'])['number'].sum()
std_df = np.std(std_df)
print(std_df)

#state that had the minimum number of total fires across all years
df_state = df.groupby(['year', 'state'])['number'].sum()
df_s = df_state.groupby('state').agg({'number':'min'}).reset_index()
print(df_s[df_s['number'] == df_s['number'].min()]['state'])

#Ex 4
#total amount of fires for the month of April for the state of Sao Paulo
#between the years of 2004 and 2014
#Abril
df_t = df[(df['year']>2003) & (df['year']<2015) & (df['month'] == 'Abril') & (df['state'] == 'Sao Paulo') ] 
df_t.head()
df_s = df_t.groupby(['year'])['number'].sum()
print(df_s)
df_sum = df_s.sum()
print(df_sum)




