#!/usr/bin/env python

from urllib.request import urlretrieve # import lib
import pandas as pd

# specify hitter and pitcher url
pitcher_url = 'https://rotogrinders.com/projected-stats/mlb-pitcher.csv?site=draftkings'
hitter_url = 'https://rotogrinders.com/projected-stats/mlb-hitter.csv?site=draftkings'

column_names = ['Player', 'Salary', 'Team', 'Position', 
                'Opponent', 'Opt', 'Pess', 'Proj']

def get_hitter_data(url = hitter_url, filename = 'hitter.csv', colnames = column_names):
    get_data = urlretrieve(url, filename) # get the data 
    hit_data = pd.read_csv(filename, names = colnames) # read the data, specify colnames
    return hit_data # return the hitter data

def get_pitcher_data(url = pitcher_url, filename = 'pitcher.csv', colnames = column_names):
    get_data = urlretrieve(url, filename) # get the data 
    pitch_data = pd.read_csv(filename, names = colnames) # read the data, specify colnames
    return pitch_data # return the pitcher data 




