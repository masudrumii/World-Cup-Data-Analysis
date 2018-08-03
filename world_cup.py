import numpy as np
import pandas as pd
from wc_functions import *
import matplotlib.pyplot as plt

# Data Files
wc_matches = 'WorldCupMatches.csv'
wc_players = 'WorldCupPlayers.csv'
wc_cups = 'WorldCups.csv'


################ Data Wrangling #############

wc_matches = pd.read_csv(wc_matches)
players = pd.read_csv(wc_players)
cups = pd.read_csv(wc_cups)


################ Data Cleaning #############

matches = wc_matches[wc_matches.notnull().any(1)]



################ Data Exploring ############


# Which teams played how many matches as Home or Away ?
home_match_played, away_match_played = home_away_counter(matches)
home_team, away_team = top_ten_home_away_team(home_match_played, away_match_played)
# Shows Bar graph of top 10 teams
#plot_bar_graph(home_team)
#plot_bar_graph(away_team)

# Most matches played by teams.
all_teams = [home_match_played, away_match_played]
matches_played = total_match_played(all_teams)


# Top 10 most matches played teams and quantity of matches. 
top_ten_most_match_played = top_ten(matches_played)
#plot_bar_graph(top_ten_most_match_played)
#plot_bar_graph(top_ten_most_match_played)

wc_years = matches['Year'].unique()

eventwise_matches = {}

for yr in wc_years:
    eventwise_matches = matches[matches['Year'] == yr]

teams = matches_played.keys()


    
