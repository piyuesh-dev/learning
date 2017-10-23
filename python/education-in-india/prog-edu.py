#!/usr/bin/env python3

# Load libraries
import numpy as np
import pandas as pd

readcols = ['statname', 'tot_population', 'literacy_rate',
	 'schools', 'sch_1', 'sch_2', 'sch_5', 'sch_6', 'sch_7', 'gsch_all', 'co_sch_all', 'girls_toilet_all']
file = '2015_16_Statewise_Secondary.csv'

"""This program tries to display various indian states over education parameters. Total population
is already divided by 1000."""

df = pd.read_csv(file, usecols=readcols)

# print(df.head(45))

df_lit = df[['statname','literacy_rate']]

df_lit = df_lit.sort_values('literacy_rate', ascending=False)

# Top 10 states as per literacy rate
print("---------------------------------------------------")
print("Top 10 states as per literacy rate")
print(df_lit.head(10))

# Top 10 states as per schools per 1000 population
df_sch_pop = df[['statname','schools','tot_population']].copy()
df_sch_pop['school_per_1000'] = df_sch_pop['schools'] / df_sch_pop['tot_population']

df_sch_pop = df_sch_pop.sort_values('school_per_1000', ascending=False)

df_sch_pop.drop(['schools', 'tot_population'], axis=1, inplace=True)
print("\n---------------------------------------------------\n")
print("Top 10 states as per schools per 1000 population")
print(df_sch_pop.round(2).head(10))

# Top 10 states as per girls schools per 1000 population
df_sch_pop_g = df[['statname','gsch_all','tot_population']].copy()
df_sch_pop_g['school_per_1000'] = df_sch_pop_g['gsch_all'] / df_sch_pop_g['tot_population']

df_sch_pop_g = df_sch_pop_g.sort_values('school_per_1000', ascending=False)

df_sch_pop_g.drop(['gsch_all', 'tot_population'], axis=1, inplace=True)
print("\n---------------------------------------------------\n")
print("Top 10 states as per girls only schools per 1000 population")
print(df_sch_pop_g.round(2).head(10))


# Top 10 states as per higher secondary schools per 1000 population
df_sch_pop_s = df[['statname','sch_1','sch_2','sch_6','sch_7','tot_population']].copy()
df_sch_pop_s['school_per_1000'] = (df_sch_pop_s['sch_1']+df_sch_pop_s['sch_2']+
			df_sch_pop_s['sch_6']+df_sch_pop_s['sch_7']) / df_sch_pop_s['tot_population']

df_sch_pop_s = df_sch_pop_s.sort_values('school_per_1000', ascending=False)

df_sch_pop_s.drop(['sch_1', 'sch_2','sch_6','sch_7','tot_population'], axis=1, inplace=True)
print("\n---------------------------------------------------\n")
print("Top 10 states as per higher secondary schools per 1000 population")
print(df_sch_pop_s.round(2).head(10))


# Bottom 10 states as population
df_pop = df[['statname','tot_population']].copy()
df_pop = df_pop.sort_values('tot_population')

print("---------------------------------------------------")
print("Bottom 10 states as per population")
print(df_pop.head(10))

