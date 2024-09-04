from http.client import FORBIDDEN
from operator import index
from re import I
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from sleeper_wrapper import League
from sleeper_wrapper import Players
import numpy as np
import time

start = time.time()

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('', scope)
client = gspread.authorize(creds)

sheet = client.open('RUFFL 2023 Season Sheet')
sh  = sheet.worksheet('Raw Data')
week = input('Enter Week: ')
standings_cell = input('Enter cell for standngs: ')
scores_cell = input('Enter cell for scores: ')
pa_cell = input('Enter cell for PA: ')
black = 985931252437962752 
blue = 981795725979815936
brown = 985932172974477312
forest = 985933433773867008
gray = 985933729388429312
green = 985934287088168960
lime = 985934465195204608
maroon = 985934680992088064
navy = 985938901581856768
orange = 985939514566770688
purple = 985940369168715776
red = 985941981413101568
sky = 985942606339252224
teal = 985943966321352704
white = 985945059495309312
yellow = 981863701940600832
emerald = 985932943119990784

class black_league:
    def __init__(self,*args):
        self.args = args

    def get_black_standings(self,*args):
        self.black_league= League(black)
        self.black_rosters = self.black_league.get_rosters()
        self.black_users = self.black_league.get_users()
        self.black_standings = self.black_league.get_standings(self.black_rosters,self.black_users)
        self.black_df = pd.DataFrame.from_dict(self.black_standings)
        self.results = (self.black_df[self.black_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_black_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('3'), self.df_black_res)
    
    def get_black_score(self,*args):
        self.black_league = League(black)
        self.black_rosters = self.black_league.get_rosters()
        self.black_users = self.black_league.get_users()
        self.black_standings = self.black_league.get_standings(self.black_rosters,self.black_users)
        self.black_matchups = self.black_league.get_matchups(week)
        self.black_lineups = self.black_league.get_lineups(self.black_rosters,self.black_matchups,self.black_users,week)
        self.black_scoreboards = self.black_league.get_scoreboards(self.black_rosters,self.black_matchups,self.black_users,week)
        self.black_df = pd.DataFrame.from_dict(self.black_standings)
        self.results = (self.black_df[self.black_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.black_scores_df = pd.DataFrame.from_dict(self.black_scoreboards)
        self.test1 = self.black_scores_df.transpose() 
        self.scores = (
            self.black_scoreboards[1][0],
            self.black_scoreboards[1][1],
            self.black_scoreboards[2][0],
            self.black_scoreboards[2][1],
            self.black_scoreboards[3][0],
            self.black_scoreboards[3][1],
            self.black_scoreboards[4][0],
            self.black_scoreboards[4][1],
            self.black_scoreboards[5][0],
            self.black_scoreboards[5][1],
            self.black_scoreboards[6][0],
            self.black_scoreboards[6][1]
        )
        self.points_against = (
            self.black_scoreboards[1][1][1],
            self.black_scoreboards[1][0][1],
            self.black_scoreboards[2][1][1],
            self.black_scoreboards[2][0][1],
            self.black_scoreboards[3][1][1],
            self.black_scoreboards[3][0][1],
            self.black_scoreboards[4][1][1],
            self.black_scoreboards[4][0][1],
            self.black_scoreboards[5][1][1],
            self.black_scoreboards[5][0][1],
            self.black_scoreboards[6][1][1],
            self.black_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('3'), self.scores)

        sh.update(pa_cell + str('3'), self.df_values)
    
class blue_league:
    def __init__(self,*args):
        self.args = args

    def get_blue_standings(self,*args):
        self.blue_league= League(blue)
        self.blue_rosters = self.blue_league.get_rosters()
        self.blue_users = self.blue_league.get_users()
        self.blue_standings = self.blue_league.get_standings(self.blue_rosters,self.blue_users)
        self.blue_df = pd.DataFrame.from_dict(self.blue_standings)
        self.results = (self.blue_df[self.blue_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_blue_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('15'), self.df_blue_res)
        
    def get_blue_score(self,*args):
        self.blue_league = League(blue)
        self.blue_rosters = self.blue_league.get_rosters()
        self.blue_users = self.blue_league.get_users()
        self.blue_standings = self.blue_league.get_standings(self.blue_rosters,self.blue_users)
        self.blue_matchups = self.blue_league.get_matchups(week)
        self.blue_lineups = self.blue_league.get_lineups(self.blue_rosters,self.blue_matchups,self.blue_users,week)
        self.blue_scoreboards = self.blue_league.get_scoreboards(self.blue_rosters,self.blue_matchups,self.blue_users,week)
        self.blue_df = pd.DataFrame.from_dict(self.blue_standings)
        self.results = (self.blue_df[self.blue_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.blue_scores_df = pd.DataFrame.from_dict(self.blue_scoreboards)
        self.test1 = self.blue_scores_df.transpose() 
        self.scores = (
            self.blue_scoreboards[1][0],
            self.blue_scoreboards[1][1],
            self.blue_scoreboards[2][0],
            self.blue_scoreboards[2][1],
            self.blue_scoreboards[3][0],
            self.blue_scoreboards[3][1],
            self.blue_scoreboards[4][0],
            self.blue_scoreboards[4][1],
            self.blue_scoreboards[5][0],
            self.blue_scoreboards[5][1],
            self.blue_scoreboards[6][0],
            self.blue_scoreboards[6][1]
        )
        self.points_against = (
            self.blue_scoreboards[1][1][1],
            self.blue_scoreboards[1][0][1],
            self.blue_scoreboards[2][1][1],
            self.blue_scoreboards[2][0][1],
            self.blue_scoreboards[3][1][1],
            self.blue_scoreboards[3][0][1],
            self.blue_scoreboards[4][1][1],
            self.blue_scoreboards[4][0][1],
            self.blue_scoreboards[5][1][1],
            self.blue_scoreboards[5][0][1],
            self.blue_scoreboards[6][1][1],
            self.blue_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('15'), self.scores)

        sh.update(pa_cell + str('15'), self.df_values)

class brown_league:
    def __init__(self,*args):
        self.args = args

    def get_brown_standings(self,*args):
        self.brown_league= League(brown)
        self.brown_rosters = self.brown_league.get_rosters()
        self.brown_users = self.brown_league.get_users()
        self.brown_standings = self.brown_league.get_standings(self.brown_rosters,self.brown_users)
        self.brown_df = pd.DataFrame.from_dict(self.brown_standings)
        self.results = (self.brown_df[self.brown_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_brown_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('27'), self.df_brown_res)
       
    def get_brown_score(self,*args):
        self.brown_league = League(brown)
        self.brown_rosters = self.brown_league.get_rosters()
        self.brown_users = self.brown_league.get_users()
        self.brown_standings = self.brown_league.get_standings(self.brown_rosters,self.brown_users)
        self.brown_matchups = self.brown_league.get_matchups(week)
        self.brown_lineups = self.brown_league.get_lineups(self.brown_rosters,self.brown_matchups,self.brown_users,week)
        self.brown_scoreboards = self.brown_league.get_scoreboards(self.brown_rosters,self.brown_matchups,self.brown_users,week)
        self.brown_df = pd.DataFrame.from_dict(self.brown_standings)
        self.results = (self.brown_df[self.brown_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.brown_scores_df = pd.DataFrame.from_dict(self.brown_scoreboards)
        self.test1 = self.brown_scores_df.transpose() 
        self.scores = (
            self.brown_scoreboards[1][0],
            self.brown_scoreboards[1][1],
            self.brown_scoreboards[2][0],
            self.brown_scoreboards[2][1],
            self.brown_scoreboards[3][0],
            self.brown_scoreboards[3][1],
            self.brown_scoreboards[4][0],
            self.brown_scoreboards[4][1],
            self.brown_scoreboards[5][0],
            self.brown_scoreboards[5][1],
            self.brown_scoreboards[6][0],
            self.brown_scoreboards[6][1]
        )
        self.points_against = (
            self.brown_scoreboards[1][1][1],
            self.brown_scoreboards[1][0][1],
            self.brown_scoreboards[2][1][1],
            self.brown_scoreboards[2][0][1],
            self.brown_scoreboards[3][1][1],
            self.brown_scoreboards[3][0][1],
            self.brown_scoreboards[4][1][1],
            self.brown_scoreboards[4][0][1],
            self.brown_scoreboards[5][1][1],
            self.brown_scoreboards[5][0][1],
            self.brown_scoreboards[6][1][1],
            self.brown_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('27'), self.scores)

        sh.update(pa_cell + str('27'), self.df_values)


class forest_league:
    def __init__(self,*args):
        self.args = args

    def get_forest_standings(self,*args):
        self.forest_league= League(forest)
        self.forest_rosters = self.forest_league.get_rosters()
        self.forest_users = self.forest_league.get_users()
        self.forest_standings = self.forest_league.get_standings(self.forest_rosters,self.forest_users)
        self.forest_df = pd.DataFrame.from_dict(self.forest_standings)
        self.results = (self.forest_df[self.forest_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_forest_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('39'), self.df_forest_res)
       # Cells for the data to be written too
        
       
    def get_forest_score(self,*args):
        self.forest_league = League(forest)
        self.forest_rosters = self.forest_league.get_rosters()
        self.forest_users = self.forest_league.get_users()
        self.forest_standings = self.forest_league.get_standings(self.forest_rosters,self.forest_users)
        self.forest_matchups = self.forest_league.get_matchups(week)
        self.forest_lineups = self.forest_league.get_lineups(self.forest_rosters,self.forest_matchups,self.forest_users,week)
        self.forest_scoreboards = self.forest_league.get_scoreboards(self.forest_rosters,self.forest_matchups,self.forest_users,week)
        self.forest_df = pd.DataFrame.from_dict(self.forest_standings)
        self.results = (self.forest_df[self.forest_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.forest_scores_df = pd.DataFrame.from_dict(self.forest_scoreboards)
        self.test1 = self.forest_scores_df.transpose() 
        self.scores = (
            self.forest_scoreboards[1][0],
            self.forest_scoreboards[1][1],
            self.forest_scoreboards[2][0],
            self.forest_scoreboards[2][1],
            self.forest_scoreboards[3][0],
            self.forest_scoreboards[3][1],
            self.forest_scoreboards[4][0],
            self.forest_scoreboards[4][1],
            self.forest_scoreboards[5][0],
            self.forest_scoreboards[5][1],
            self.forest_scoreboards[6][0],
            self.forest_scoreboards[6][1]
        )
        self.points_against = (
            self.forest_scoreboards[1][1][1],
            self.forest_scoreboards[1][0][1],
            self.forest_scoreboards[2][1][1],
            self.forest_scoreboards[2][0][1],
            self.forest_scoreboards[3][1][1],
            self.forest_scoreboards[3][0][1],
            self.forest_scoreboards[4][1][1],
            self.forest_scoreboards[4][0][1],
            self.forest_scoreboards[5][1][1],
            self.forest_scoreboards[5][0][1],
            self.forest_scoreboards[6][1][1],
            self.forest_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('39'), self.scores)

        sh.update(pa_cell + str('39'), self.df_values)

class gray_league:
    def __init__(self,*args):
        self.args = args

    def get_gray_standings(self,*args):
        self.gray_league= League(gray)
        self.gray_rosters = self.gray_league.get_rosters()
        self.gray_users = self.gray_league.get_users()
        self.gray_standings = self.gray_league.get_standings(self.gray_rosters,self.gray_users)
        self.gray_df = pd.DataFrame.from_dict(self.gray_standings)
        self.results = (self.gray_df[self.gray_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_grey_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('51'), self.df_grey_res)
       # Cells for the data to be written too
        
       
    def get_gray_score(self,*args):
        self.gray_league = League(gray)
        self.gray_rosters = self.gray_league.get_rosters()
        self.gray_users = self.gray_league.get_users()
        self.gray_standings = self.gray_league.get_standings(self.gray_rosters,self.gray_users)
        self.gray_matchups = self.gray_league.get_matchups(week)
        self.gray_lineups = self.gray_league.get_lineups(self.gray_rosters,self.gray_matchups,self.gray_users,week)
        self.gray_scoreboards = self.gray_league.get_scoreboards(self.gray_rosters,self.gray_matchups,self.gray_users,week)
        self.gray_df = pd.DataFrame.from_dict(self.gray_standings)
        self.results = (self.gray_df[self.gray_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.gray_scores_df = pd.DataFrame.from_dict(self.gray_scoreboards)
        self.test1 = self.gray_scores_df.transpose() 
        self.scores = (
            self.gray_scoreboards[1][0],
            self.gray_scoreboards[1][1],
            self.gray_scoreboards[2][0],
            self.gray_scoreboards[2][1],
            self.gray_scoreboards[3][0],
            self.gray_scoreboards[3][1],
            self.gray_scoreboards[4][0],
            self.gray_scoreboards[4][1],
            self.gray_scoreboards[5][0],
            self.gray_scoreboards[5][1],
            self.gray_scoreboards[6][0],
            self.gray_scoreboards[6][1]
        )
        self.points_against = (
            self.gray_scoreboards[1][1][1],
            self.gray_scoreboards[1][0][1],
            self.gray_scoreboards[2][1][1],
            self.gray_scoreboards[2][0][1],
            self.gray_scoreboards[3][1][1],
            self.gray_scoreboards[3][0][1],
            self.gray_scoreboards[4][1][1],
            self.gray_scoreboards[4][0][1],
            self.gray_scoreboards[5][1][1],
            self.gray_scoreboards[5][0][1],
            self.gray_scoreboards[6][1][1],
            self.gray_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('51'), self.scores)

        sh.update(pa_cell + str('51'), self.df_values)


class green_league:
    def __init__(self,*args):
        self.args = args

    def get_green_standings(self,*args):
        self.green_league= League(green)
        self.green_rosters = self.green_league.get_rosters()
        self.green_users = self.green_league.get_users()
        self.green_standings = self.green_league.get_standings(self.green_rosters,self.green_users)
        self.green_df = pd.DataFrame.from_dict(self.green_standings)
        self.results = (self.green_df[self.green_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_green_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('63'), self.df_green_res)
       # Cells for the data to be written too
        
       
    def get_green_score(self,*args):
        self.green_league = League(green)
        self.green_rosters = self.green_league.get_rosters()
        self.green_users = self.green_league.get_users()
        self.green_standings = self.green_league.get_standings(self.green_rosters,self.green_users)
        self.green_matchups = self.green_league.get_matchups(week)
        self.green_lineups = self.green_league.get_lineups(self.green_rosters,self.green_matchups,self.green_users,week)
        self.green_scoreboards = self.green_league.get_scoreboards(self.green_rosters,self.green_matchups,self.green_users,week)
        self.green_df = pd.DataFrame.from_dict(self.green_standings)
        self.results = (self.green_df[self.green_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.green_scores_df = pd.DataFrame.from_dict(self.green_scoreboards)
        self.test1 = self.green_scores_df.transpose() 
        self.scores = (
            self.green_scoreboards[1][0],
            self.green_scoreboards[1][1],
            self.green_scoreboards[2][0],
            self.green_scoreboards[2][1],
            self.green_scoreboards[3][0],
            self.green_scoreboards[3][1],
            self.green_scoreboards[4][0],
            self.green_scoreboards[4][1],
            self.green_scoreboards[5][0],
            self.green_scoreboards[5][1],
            self.green_scoreboards[6][0],
            self.green_scoreboards[6][1]
        )
        self.points_against = (
            self.green_scoreboards[1][1][1],
            self.green_scoreboards[1][0][1],
            self.green_scoreboards[2][1][1],
            self.green_scoreboards[2][0][1],
            self.green_scoreboards[3][1][1],
            self.green_scoreboards[3][0][1],
            self.green_scoreboards[4][1][1],
            self.green_scoreboards[4][0][1],
            self.green_scoreboards[5][1][1],
            self.green_scoreboards[5][0][1],
            self.green_scoreboards[6][1][1],
            self.green_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('63'), self.scores)

        sh.update(pa_cell + str('63'), self.df_values)


class lime_league:
    def __init__(self,*args):
        self.args = args

    def get_lime_standings(self,*args):
        self.lime_league= League(lime)
        self.lime_rosters = self.lime_league.get_rosters()
        self.lime_users = self.lime_league.get_users()
        self.lime_standings = self.lime_league.get_standings(self.lime_rosters,self.lime_users)
        self.lime_df = pd.DataFrame.from_dict(self.lime_standings)
        self.results = (self.lime_df[self.lime_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_lime_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('75'), self.df_lime_res)
       # Cells for the data to be written too
               
    def get_lime_score(self,*args):
        self.lime_league = League(lime)
        self.lime_rosters = self.lime_league.get_rosters()
        self.lime_users = self.lime_league.get_users()
        self.lime_standings = self.lime_league.get_standings(self.lime_rosters,self.lime_users)
        self.lime_matchups = self.lime_league.get_matchups(week)
        self.lime_lineups = self.lime_league.get_lineups(self.lime_rosters,self.lime_matchups,self.lime_users,week)
        self.lime_scoreboards = self.lime_league.get_scoreboards(self.lime_rosters,self.lime_matchups,self.lime_users,week)
        self.lime_df = pd.DataFrame.from_dict(self.lime_standings)
        self.results = (self.lime_df[self.lime_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.lime_scores_df = pd.DataFrame.from_dict(self.lime_scoreboards)
        self.test1 = self.lime_scores_df.transpose() 
        self.scores = (
            self.lime_scoreboards[1][0],
            self.lime_scoreboards[1][1],
            self.lime_scoreboards[2][0],
            self.lime_scoreboards[2][1],
            self.lime_scoreboards[3][0],
            self.lime_scoreboards[3][1],
            self.lime_scoreboards[4][0],
            self.lime_scoreboards[4][1],
            self.lime_scoreboards[5][0],
            self.lime_scoreboards[5][1],
            self.lime_scoreboards[6][0],
            self.lime_scoreboards[6][1]
        )
        self.points_against = (
            self.lime_scoreboards[1][1][1],
            self.lime_scoreboards[1][0][1],
            self.lime_scoreboards[2][1][1],
            self.lime_scoreboards[2][0][1],
            self.lime_scoreboards[3][1][1],
            self.lime_scoreboards[3][0][1],
            self.lime_scoreboards[4][1][1],
            self.lime_scoreboards[4][0][1],
            self.lime_scoreboards[5][1][1],
            self.lime_scoreboards[5][0][1],
            self.lime_scoreboards[6][1][1],
            self.lime_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('75'), self.scores)

        sh.update(pa_cell + str('75'), self.df_values)


class maroon_league:
    def __init__(self,*args):
        self.args = args

    def get_maroon_standings(self,*args):
        self.maroon_league= League(maroon)
        self.maroon_rosters = self.maroon_league.get_rosters()
        self.maroon_users = self.maroon_league.get_users()
        self.maroon_standings = self.maroon_league.get_standings(self.maroon_rosters,self.maroon_users)
        self.maroon_df = pd.DataFrame.from_dict(self.maroon_standings)
        self.results = (self.maroon_df[self.maroon_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_maroon_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('87'), self.df_maroon_res)
       # Cells for the data to be written too
        
       
    def get_maroon_score(self,*args):
        self.maroon_league = League(maroon)
        self.maroon_rosters = self.maroon_league.get_rosters()
        self.maroon_users = self.maroon_league.get_users()
        self.maroon_standings = self.maroon_league.get_standings(self.maroon_rosters,self.maroon_users)
        self.maroon_matchups = self.maroon_league.get_matchups(week)
        self.maroon_lineups = self.maroon_league.get_lineups(self.maroon_rosters,self.maroon_matchups,self.maroon_users,week)
        self.maroon_scoreboards = self.maroon_league.get_scoreboards(self.maroon_rosters,self.maroon_matchups,self.maroon_users,week)
        self.maroon_df = pd.DataFrame.from_dict(self.maroon_standings)
        self.results = (self.maroon_df[self.maroon_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.maroon_scores_df = pd.DataFrame.from_dict(self.maroon_scoreboards)
        self.test1 = self.maroon_scores_df.transpose() 
        self.scores = (
            self.maroon_scoreboards[1][0],
            self.maroon_scoreboards[1][1],
            self.maroon_scoreboards[2][0],
            self.maroon_scoreboards[2][1],
            self.maroon_scoreboards[3][0],
            self.maroon_scoreboards[3][1],
            self.maroon_scoreboards[4][0],
            self.maroon_scoreboards[4][1],
            self.maroon_scoreboards[5][0],
            self.maroon_scoreboards[5][1],
            self.maroon_scoreboards[6][0],
            self.maroon_scoreboards[6][1]
        )
        self.points_against = (
            self.maroon_scoreboards[1][1][1],
            self.maroon_scoreboards[1][0][1],
            self.maroon_scoreboards[2][1][1],
            self.maroon_scoreboards[2][0][1],
            self.maroon_scoreboards[3][1][1],
            self.maroon_scoreboards[3][0][1],
            self.maroon_scoreboards[4][1][1],
            self.maroon_scoreboards[4][0][1],
            self.maroon_scoreboards[5][1][1],
            self.maroon_scoreboards[5][0][1],
            self.maroon_scoreboards[6][1][1],
            self.maroon_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('87'), self.scores)

        sh.update(pa_cell + str('87'), self.df_values)



class navy_league:
    def __init__(self,*args):
        self.args = args

    def get_navy_standings(self,*args):
        self.navy_league= League(navy)
        self.navy_rosters = self.navy_league.get_rosters()
        self.navy_users = self.navy_league.get_users()
        self.navy_standings = self.navy_league.get_standings(self.navy_rosters,self.navy_users)
        self.navy_df = pd.DataFrame.from_dict(self.navy_standings)
        self.results = (self.navy_df[self.navy_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_navy_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('99'), self.df_navy_res)
       # Cells for the data to be written too
        
       
    def get_navy_score(self,*args):
        self.navy_league = League(navy)
        self.navy_rosters = self.navy_league.get_rosters()
        self.navy_users = self.navy_league.get_users()
        self.navy_standings = self.navy_league.get_standings(self.navy_rosters,self.navy_users)
        self.navy_matchups = self.navy_league.get_matchups(week)
        self.navy_lineups = self.navy_league.get_lineups(self.navy_rosters,self.navy_matchups,self.navy_users,week)
        self.navy_scoreboards = self.navy_league.get_scoreboards(self.navy_rosters,self.navy_matchups,self.navy_users,week)
        self.navy_df = pd.DataFrame.from_dict(self.navy_standings)
        self.results = (self.navy_df[self.navy_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.navy_scores_df = pd.DataFrame.from_dict(self.navy_scoreboards)
        self.test1 = self.navy_scores_df.transpose() 
        self.scores = (
            self.navy_scoreboards[1][0],
            self.navy_scoreboards[1][1],
            self.navy_scoreboards[2][0],
            self.navy_scoreboards[2][1],
            self.navy_scoreboards[3][0],
            self.navy_scoreboards[3][1],
            self.navy_scoreboards[4][0],
            self.navy_scoreboards[4][1],
            self.navy_scoreboards[5][0],
            self.navy_scoreboards[5][1],
            self.navy_scoreboards[6][0],
            self.navy_scoreboards[6][1]
        )
        self.points_against = (
            self.navy_scoreboards[1][1][1],
            self.navy_scoreboards[1][0][1],
            self.navy_scoreboards[2][1][1],
            self.navy_scoreboards[2][0][1],
            self.navy_scoreboards[3][1][1],
            self.navy_scoreboards[3][0][1],
            self.navy_scoreboards[4][1][1],
            self.navy_scoreboards[4][0][1],
            self.navy_scoreboards[5][1][1],
            self.navy_scoreboards[5][0][1],
            self.navy_scoreboards[6][1][1],
            self.navy_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('99'), self.scores)

        sh.update(pa_cell + str('99'), self.df_values)



class orange_league:
    def __init__(self,*args):
        self.args = args

    def get_orange_standings(self,*args):
        self.orange_league= League(orange)
        self.orange_rosters = self.orange_league.get_rosters()
        self.orange_users = self.orange_league.get_users()
        self.orange_standings = self.orange_league.get_standings(self.orange_rosters,self.orange_users)
        self.orange_df = pd.DataFrame.from_dict(self.orange_standings)
        self.results = (self.orange_df[self.orange_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_orange_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('111'), self.df_orange_res)
       # Cells for the data to be written too
        
       
    def get_orange_score(self,*args):
        self.orange_league = League(orange)
        self.orange_rosters = self.orange_league.get_rosters()
        self.orange_users = self.orange_league.get_users()
        self.orange_standings = self.orange_league.get_standings(self.orange_rosters,self.orange_users)
        self.orange_matchups = self.orange_league.get_matchups(week)
        self.orange_lineups = self.orange_league.get_lineups(self.orange_rosters,self.orange_matchups,self.orange_users,week)
        self.orange_scoreboards = self.orange_league.get_scoreboards(self.orange_rosters,self.orange_matchups,self.orange_users,week)
        self.orange_df = pd.DataFrame.from_dict(self.orange_standings)
        self.results = (self.orange_df[self.orange_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.orange_scores_df = pd.DataFrame.from_dict(self.orange_scoreboards)
        self.test1 = self.orange_scores_df.transpose() 
        self.scores = (
            self.orange_scoreboards[1][0],
            self.orange_scoreboards[1][1],
            self.orange_scoreboards[2][0],
            self.orange_scoreboards[2][1],
            self.orange_scoreboards[3][0],
            self.orange_scoreboards[3][1],
            self.orange_scoreboards[4][0],
            self.orange_scoreboards[4][1],
            self.orange_scoreboards[5][0],
            self.orange_scoreboards[5][1],
            self.orange_scoreboards[6][0],
            self.orange_scoreboards[6][1]
        )
        self.points_against = (
            self.orange_scoreboards[1][1][1],
            self.orange_scoreboards[1][0][1],
            self.orange_scoreboards[2][1][1],
            self.orange_scoreboards[2][0][1],
            self.orange_scoreboards[3][1][1],
            self.orange_scoreboards[3][0][1],
            self.orange_scoreboards[4][1][1],
            self.orange_scoreboards[4][0][1],
            self.orange_scoreboards[5][1][1],
            self.orange_scoreboards[5][0][1],
            self.orange_scoreboards[6][1][1],
            self.orange_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('111'), self.scores)

        sh.update(pa_cell + str('111'), self.df_values)



class purple_league:
    def __init__(self,*args):
        self.args = args

    def get_purple_standings(self,*args):
        self.purple_league= League(purple)
        self.purple_rosters = self.purple_league.get_rosters()
        self.purple_users = self.purple_league.get_users()
        self.purple_standings = self.purple_league.get_standings(self.purple_rosters,self.purple_users)
        self.purple_df = pd.DataFrame.from_dict(self.purple_standings)
        self.results = (self.purple_df[self.purple_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_purple_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('123'), self.df_purple_res)
       # Cells for the data to be written too
        
       
    def get_purple_score(self,*args):
        self.purple_league = League(purple)
        self.purple_rosters = self.purple_league.get_rosters()
        self.purple_users = self.purple_league.get_users()
        self.purple_standings = self.purple_league.get_standings(self.purple_rosters,self.purple_users)
        self.purple_matchups = self.purple_league.get_matchups(week)
        self.purple_lineups = self.purple_league.get_lineups(self.purple_rosters,self.purple_matchups,self.purple_users,week)
        self.purple_scoreboards = self.purple_league.get_scoreboards(self.purple_rosters,self.purple_matchups,self.purple_users,week)
        self.purple_df = pd.DataFrame.from_dict(self.purple_standings)
        self.results = (self.purple_df[self.purple_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.purple_scores_df = pd.DataFrame.from_dict(self.purple_scoreboards)
        self.test1 = self.purple_scores_df.transpose() 
        self.scores = (
            self.purple_scoreboards[1][0],
            self.purple_scoreboards[1][1],
            self.purple_scoreboards[2][0],
            self.purple_scoreboards[2][1],
            self.purple_scoreboards[3][0],
            self.purple_scoreboards[3][1],
            self.purple_scoreboards[4][0],
            self.purple_scoreboards[4][1],
            self.purple_scoreboards[5][0],
            self.purple_scoreboards[5][1],
            self.purple_scoreboards[6][0],
            self.purple_scoreboards[6][1]
        )
        self.points_against = (
            self.purple_scoreboards[1][1][1],
            self.purple_scoreboards[1][0][1],
            self.purple_scoreboards[2][1][1],
            self.purple_scoreboards[2][0][1],
            self.purple_scoreboards[3][1][1],
            self.purple_scoreboards[3][0][1],
            self.purple_scoreboards[4][1][1],
            self.purple_scoreboards[4][0][1],
            self.purple_scoreboards[5][1][1],
            self.purple_scoreboards[5][0][1],
            self.purple_scoreboards[6][1][1],
            self.purple_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('123'), self.scores)

        sh.update(pa_cell + str('123'), self.df_values)


class red_league:
    def __init__(self,*args):
        self.args = args

    def get_red_standings(self,*args):
        self.red_league= League(red)
        self.red_rosters = self.red_league.get_rosters()
        self.red_users = self.red_league.get_users()
        self.red_standings = self.red_league.get_standings(self.red_rosters,self.red_users)
        self.red_df = pd.DataFrame.from_dict(self.red_standings)
        self.results = (self.red_df[self.red_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_red_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('135'), self.df_red_res)
       # Cells for the data to be written too
        
       
    def get_red_score(self,*args):
        self.red_league = League(red)
        self.red_rosters = self.red_league.get_rosters()
        self.red_users = self.red_league.get_users()
        self.red_standings = self.red_league.get_standings(self.red_rosters,self.red_users)
        self.red_matchups = self.red_league.get_matchups(week)
        self.red_lineups = self.red_league.get_lineups(self.red_rosters,self.red_matchups,self.red_users,week)
        self.red_scoreboards = self.red_league.get_scoreboards(self.red_rosters,self.red_matchups,self.red_users,week)
        self.red_df = pd.DataFrame.from_dict(self.red_standings)
        self.results = (self.red_df[self.red_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.red_scores_df = pd.DataFrame.from_dict(self.red_scoreboards)
        self.test1 = self.red_scores_df.transpose() 
        self.scores = (
            self.red_scoreboards[1][0],
            self.red_scoreboards[1][1],
            self.red_scoreboards[2][0],
            self.red_scoreboards[2][1],
            self.red_scoreboards[3][0],
            self.red_scoreboards[3][1],
            self.red_scoreboards[4][0],
            self.red_scoreboards[4][1],
            self.red_scoreboards[5][0],
            self.red_scoreboards[5][1],
            self.red_scoreboards[6][0],
            self.red_scoreboards[6][1]
        )
        self.points_against = (
            self.red_scoreboards[1][1][1],
            self.red_scoreboards[1][0][1],
            self.red_scoreboards[2][1][1],
            self.red_scoreboards[2][0][1],
            self.red_scoreboards[3][1][1],
            self.red_scoreboards[3][0][1],
            self.red_scoreboards[4][1][1],
            self.red_scoreboards[4][0][1],
            self.red_scoreboards[5][1][1],
            self.red_scoreboards[5][0][1],
            self.red_scoreboards[6][1][1],
            self.red_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('135'), self.scores)

        sh.update(pa_cell + str('135'), self.df_values)


class sky_league:
    def __init__(self,*args):
        self.args = args

    def get_sky_standings(self,*args):
        self.sky_league= League(sky)
        self.sky_rosters = self.sky_league.get_rosters()
        self.sky_users = self.sky_league.get_users()
        self.sky_standings = self.sky_league.get_standings(self.sky_rosters,self.sky_users)
        self.sky_df = pd.DataFrame.from_dict(self.sky_standings)
        self.results = (self.sky_df[self.sky_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_sky_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('147'), self.df_sky_res)
       # Cells for the data to be written too
        
       
    def get_sky_score(self,*args):
        self.sky_league = League(sky)
        self.sky_rosters = self.sky_league.get_rosters()
        self.sky_users = self.sky_league.get_users()
        self.sky_standings = self.sky_league.get_standings(self.sky_rosters,self.sky_users)
        self.sky_matchups = self.sky_league.get_matchups(week)
        self.sky_lineups = self.sky_league.get_lineups(self.sky_rosters,self.sky_matchups,self.sky_users,week)
        self.sky_scoreboards = self.sky_league.get_scoreboards(self.sky_rosters,self.sky_matchups,self.sky_users,week)
        self.sky_df = pd.DataFrame.from_dict(self.sky_standings)
        self.results = (self.sky_df[self.sky_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.sky_scores_df = pd.DataFrame.from_dict(self.sky_scoreboards)
        self.test1 = self.sky_scores_df.transpose() 
        self.scores = (
            self.sky_scoreboards[1][0],
            self.sky_scoreboards[1][1],
            self.sky_scoreboards[2][0],
            self.sky_scoreboards[2][1],
            self.sky_scoreboards[3][0],
            self.sky_scoreboards[3][1],
            self.sky_scoreboards[4][0],
            self.sky_scoreboards[4][1],
            self.sky_scoreboards[5][0],
            self.sky_scoreboards[5][1],
            self.sky_scoreboards[6][0],
            self.sky_scoreboards[6][1]
        )
        self.points_against = (
            self.sky_scoreboards[1][1][1],
            self.sky_scoreboards[1][0][1],
            self.sky_scoreboards[2][1][1],
            self.sky_scoreboards[2][0][1],
            self.sky_scoreboards[3][1][1],
            self.sky_scoreboards[3][0][1],
            self.sky_scoreboards[4][1][1],
            self.sky_scoreboards[4][0][1],
            self.sky_scoreboards[5][1][1],
            self.sky_scoreboards[5][0][1],
            self.sky_scoreboards[6][1][1],
            self.sky_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('147'), self.scores)

        sh.update(pa_cell + str('147'), self.df_values)


class teal_league:
    def __init__(self,*args):
        self.args = args

    def get_teal_standings(self,*args):
        self.teal_league= League(teal)
        self.teal_rosters = self.teal_league.get_rosters()
        self.teal_users = self.teal_league.get_users()
        self.teal_standings = self.teal_league.get_standings(self.teal_rosters,self.teal_users)
        self.teal_df = pd.DataFrame.from_dict(self.teal_standings)
        self.results = (self.teal_df[self.teal_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_teal_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('159'), self.df_teal_res)
       # Cells for the data to be written too
        
       
    def get_teal_score(self,*args):
        self.teal_league = League(teal)
        self.teal_rosters = self.teal_league.get_rosters()
        self.teal_users = self.teal_league.get_users()
        self.teal_standings = self.teal_league.get_standings(self.teal_rosters,self.teal_users)
        self.teal_matchups = self.teal_league.get_matchups(week)
        self.teal_lineups = self.teal_league.get_lineups(self.teal_rosters,self.teal_matchups,self.teal_users,week)
        self.teal_scoreboards = self.teal_league.get_scoreboards(self.teal_rosters,self.teal_matchups,self.teal_users,week)
        self.teal_df = pd.DataFrame.from_dict(self.teal_standings)
        self.results = (self.teal_df[self.teal_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.teal_scores_df = pd.DataFrame.from_dict(self.teal_scoreboards)
        self.test1 = self.teal_scores_df.transpose() 
        self.scores = (
            self.teal_scoreboards[1][0],
            self.teal_scoreboards[1][1],
            self.teal_scoreboards[2][0],
            self.teal_scoreboards[2][1],
            self.teal_scoreboards[3][0],
            self.teal_scoreboards[3][1],
            self.teal_scoreboards[4][0],
            self.teal_scoreboards[4][1],
            self.teal_scoreboards[5][0],
            self.teal_scoreboards[5][1],
            self.teal_scoreboards[6][0],
            self.teal_scoreboards[6][1]
        )
        self.points_against = (
            self.teal_scoreboards[1][1][1],
            self.teal_scoreboards[1][0][1],
            self.teal_scoreboards[2][1][1],
            self.teal_scoreboards[2][0][1],
            self.teal_scoreboards[3][1][1],
            self.teal_scoreboards[3][0][1],
            self.teal_scoreboards[4][1][1],
            self.teal_scoreboards[4][0][1],
            self.teal_scoreboards[5][1][1],
            self.teal_scoreboards[5][0][1],
            self.teal_scoreboards[6][1][1],
            self.teal_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('159'), self.scores)

        sh.update(pa_cell + str('159'), self.df_values)



class white_league:
    def __init__(self,*args):
        self.args = args

    def get_white_standings(self,*args):
        self.white_league= League(white)
        self.white_rosters = self.white_league.get_rosters()
        self.white_users = self.white_league.get_users()
        self.white_standings = self.white_league.get_standings(self.white_rosters,self.white_users)
        self.white_df = pd.DataFrame.from_dict(self.white_standings)
        self.results = (self.white_df[self.white_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_white_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('171'), self.df_white_res)
       # Cells for the data to be written too
        
       
    def get_white_score(self,*args):
        self.white_league = League(white)
        self.white_rosters = self.white_league.get_rosters()
        self.white_users = self.white_league.get_users()
        self.white_standings = self.white_league.get_standings(self.white_rosters,self.white_users)
        self.white_matchups = self.white_league.get_matchups(week)
        self.white_lineups = self.white_league.get_lineups(self.white_rosters,self.white_matchups,self.white_users,week)
        self.white_scoreboards = self.white_league.get_scoreboards(self.white_rosters,self.white_matchups,self.white_users,week)
        self.white_df = pd.DataFrame.from_dict(self.white_standings)
        self.results = (self.white_df[self.white_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.white_scores_df = pd.DataFrame.from_dict(self.white_scoreboards)
        self.test1 = self.white_scores_df.transpose() 
        self.scores = (
            self.white_scoreboards[1][0],
            self.white_scoreboards[1][1],
            self.white_scoreboards[2][0],
            self.white_scoreboards[2][1],
            self.white_scoreboards[3][0],
            self.white_scoreboards[3][1],
            self.white_scoreboards[4][0],
            self.white_scoreboards[4][1],
            self.white_scoreboards[5][0],
            self.white_scoreboards[5][1],
            self.white_scoreboards[6][0],
            self.white_scoreboards[6][1]
        )
        self.points_against = (
            self.white_scoreboards[1][1][1],
            self.white_scoreboards[1][0][1],
            self.white_scoreboards[2][1][1],
            self.white_scoreboards[2][0][1],
            self.white_scoreboards[3][1][1],
            self.white_scoreboards[3][0][1],
            self.white_scoreboards[4][1][1],
            self.white_scoreboards[4][0][1],
            self.white_scoreboards[5][1][1],
            self.white_scoreboards[5][0][1],
            self.white_scoreboards[6][1][1],
            self.white_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('171'), self.scores)

        sh.update(pa_cell + str('171'), self.df_values)



class yellow_league:
    def __init__(self,*args):
        self.args = args

    def get_yellow_standings(self,*args):
        self.yellow_league= League(yellow)
        self.yellow_rosters = self.yellow_league.get_rosters()
        self.yellow_users = self.yellow_league.get_users()
        self.yellow_standings = self.yellow_league.get_standings(self.yellow_rosters,self.yellow_users)
        self.yellow_df = pd.DataFrame.from_dict(self.yellow_standings)
        self.results = (self.yellow_df[self.yellow_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_yellow_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('183'), self.df_yellow_res)
       # Cells for the data to be written too
        
       
    def get_yellow_score(self,*args):
        self.yellow_league = League(yellow)
        self.yellow_rosters = self.yellow_league.get_rosters()
        self.yellow_users = self.yellow_league.get_users()
        self.yellow_standings = self.yellow_league.get_standings(self.yellow_rosters,self.yellow_users)
        self.yellow_matchups = self.yellow_league.get_matchups(week)
        self.yellow_lineups = self.yellow_league.get_lineups(self.yellow_rosters,self.yellow_matchups,self.yellow_users,week)
        self.yellow_scoreboards = self.yellow_league.get_scoreboards(self.yellow_rosters,self.yellow_matchups,self.yellow_users,week)
        self.yellow_df = pd.DataFrame.from_dict(self.yellow_standings)
        self.results = (self.yellow_df[self.yellow_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.yellow_scores_df = pd.DataFrame.from_dict(self.yellow_scoreboards)
        self.test1 = self.yellow_scores_df.transpose() 
        self.scores = (
            self.yellow_scoreboards[1][0],
            self.yellow_scoreboards[1][1],
            self.yellow_scoreboards[2][0],
            self.yellow_scoreboards[2][1],
            self.yellow_scoreboards[3][0],
            self.yellow_scoreboards[3][1],
            self.yellow_scoreboards[4][0],
            self.yellow_scoreboards[4][1],
            self.yellow_scoreboards[5][0],
            self.yellow_scoreboards[5][1],
            self.yellow_scoreboards[6][0],
            self.yellow_scoreboards[6][1]
        )
        self.points_against = (
            self.yellow_scoreboards[1][1][1],
            self.yellow_scoreboards[1][0][1],
            self.yellow_scoreboards[2][1][1],
            self.yellow_scoreboards[2][0][1],
            self.yellow_scoreboards[3][1][1],
            self.yellow_scoreboards[3][0][1],
            self.yellow_scoreboards[4][1][1],
            self.yellow_scoreboards[4][0][1],
            self.yellow_scoreboards[5][1][1],
            self.yellow_scoreboards[5][0][1],
            self.yellow_scoreboards[6][1][1],
            self.yellow_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('183'), self.scores)

        sh.update(pa_cell + str('183'), self.df_values)



class emerald_league:
    def __init__(self,*args):
        self.args = args

    def get_emerald_standings(self,*args):
        self.emerald_league= League(emerald)
        self.emerald_rosters = self.emerald_league.get_rosters()
        self.emerald_users = self.emerald_league.get_users()
        self.emerald_standings = self.emerald_league.get_standings(self.emerald_rosters,self.emerald_users)
        self.emerald_df = pd.DataFrame.from_dict(self.emerald_standings)
        self.results = (self.emerald_df[self.emerald_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.df_emerald_res = self.table_data.values.tolist()
        sh.update(standings_cell + str('195'), self.df_emerald_res)
       # Cells for the data to be written too
        
       
    def get_emerald_score(self,*args):
        self.emerald_league = League(emerald)
        self.emerald_rosters = self.emerald_league.get_rosters()
        self.emerald_users = self.emerald_league.get_users()
        self.emerald_standings = self.emerald_league.get_standings(self.emerald_rosters,self.emerald_users)
        self.emerald_matchups = self.emerald_league.get_matchups(week)
        self.emerald_lineups = self.emerald_league.get_lineups(self.emerald_rosters,self.emerald_matchups,self.emerald_users,week)
        self.emerald_scoreboards = self.emerald_league.get_scoreboards(self.emerald_rosters,self.emerald_matchups,self.emerald_users,week)
        self.emerald_df = pd.DataFrame.from_dict(self.emerald_standings)
        self.results = (self.emerald_df[self.emerald_df.columns[[0,1,2,3,4]]])
        self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
        self.table_data = self.results.drop([1,2], axis=1)
        self.emerald_scores_df = pd.DataFrame.from_dict(self.emerald_scoreboards)
        self.test1 = self.emerald_scores_df.transpose() 
        self.scores = (
            self.emerald_scoreboards[1][0],
            self.emerald_scoreboards[1][1],
            self.emerald_scoreboards[2][0],
            self.emerald_scoreboards[2][1],
            self.emerald_scoreboards[3][0],
            self.emerald_scoreboards[3][1],
            self.emerald_scoreboards[4][0],
            self.emerald_scoreboards[4][1],
            self.emerald_scoreboards[5][0],
            self.emerald_scoreboards[5][1],
            self.emerald_scoreboards[6][0],
            self.emerald_scoreboards[6][1]
        )
        self.points_against = (
            self.emerald_scoreboards[1][1][1],
            self.emerald_scoreboards[1][0][1],
            self.emerald_scoreboards[2][1][1],
            self.emerald_scoreboards[2][0][1],
            self.emerald_scoreboards[3][1][1],
            self.emerald_scoreboards[3][0][1],
            self.emerald_scoreboards[4][1][1],
            self.emerald_scoreboards[4][0][1],
            self.emerald_scoreboards[5][1][1],
            self.emerald_scoreboards[5][0][1],
            self.emerald_scoreboards[6][1][1],
            self.emerald_scoreboards[6][0][1]
        )
        self.df = pd.DataFrame.from_dict(self.scores)
        self.pa_df = pd.DataFrame.from_dict(self.points_against)
        self.df_values = self.pa_df.values.tolist()
        sh.update(scores_cell + str('195'), self.scores)

        sh.update(pa_cell + str('195'), self.df_values)


black_league().get_black_score()
black_league().get_black_standings()
blue_league().get_blue_standings()
blue_league().get_blue_score()
brown_league().get_brown_standings()
brown_league().get_brown_score()
forest_league().get_forest_standings()
forest_league().get_forest_score()
gray_league().get_gray_standings()
gray_league().get_gray_score()
green_league().get_green_standings()
green_league().get_green_score()
lime_league().get_lime_standings()
lime_league().get_lime_score()
maroon_league().get_maroon_standings()
maroon_league().get_maroon_score()
navy_league().get_navy_standings()
navy_league().get_navy_score()
orange_league().get_orange_standings()
orange_league().get_orange_score()
purple_league().get_purple_standings()
purple_league().get_purple_score()
red_league().get_red_standings()
red_league().get_red_score()
sky_league().get_sky_standings()
sky_league().get_sky_score()
teal_league().get_teal_standings()
teal_league().get_teal_score()
white_league().get_white_standings()
white_league().get_white_score()
yellow_league().get_yellow_standings()
yellow_league().get_yellow_score()
emerald_league().get_emerald_standings()
emerald_league().get_emerald_score()

end = time.time()

total_time = end - start

print("\n"+ str(total_time))
