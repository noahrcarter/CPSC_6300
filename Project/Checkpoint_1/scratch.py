

import pandas as pd
import os

total = 0
total_unique = 0

df = pd.read_csv('data/games.csv')
num_observations = len(df)
total+= num_observations
print("observations of games = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique games = ", str(num_unique))

df = pd.read_csv('data/player_play.csv')
num_observations = len(df)
total+= num_observations
print("observations of player_play = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique player_play = ", str(num_unique))

df = pd.read_csv('data/players.csv')
num_observations = len(df)
total+= num_observations
print("observations of players = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique players = ", str(num_unique))

df = pd.read_csv('data/plays.csv')
num_observations = len(df)
total+= num_observations
print("observations of plays = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique plays = ", str(num_unique))

df = pd.read_csv('data/tracking_week_1.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_1 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_1 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_2.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_2 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_2 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_3.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_3 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_3 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_4.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_4 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_4 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_5.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_5 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_5 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_6.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_6 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_6 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_7.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_7 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_7 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_8.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_8 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_8 = ", str(num_unique))

df = pd.read_csv('data/tracking_week_9.csv')
num_observations = len(df)
total+= num_observations
print("observations of tracking_week_9 = ", str(num_observations))
num_unique = len(df.drop_duplicates())
total_unique += num_unique
print("unique tracking_week_9 = ", str(num_unique))

print("total observations = ", total)
print("total unique observations = ", total_unique)