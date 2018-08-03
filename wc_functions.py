import matplotlib.pyplot as plt
import operator

def home_away_counter(matches):
    '''
    Following function counts the home or away match played.
    returns two separate dictionaries. Both of the dictionaries
    are sorted by values in descending order.
    
    KEY: Team Name ( String ).
    VALUE: Match Played ( Integer ).
    '''
    
    home_match_played = {}
    away_match_played = {}

    for index, match in matches.iterrows():
    
        home_team = match['Home Team Name']
        away_team = match['Away Team Name']
    
        if home_team in home_match_played.keys():
            home_match_played[home_team] += 1
        else:
            home_match_played[home_team] = 1

        if away_team in away_match_played.keys():
            away_match_played[away_team] += 1
        else:
            away_match_played[away_team] = 1

    # Sort the dictionary by values in descending order
    home_match_played = sorted(home_match_played.items(), key=operator.itemgetter(1), reverse=True)
    away_match_played = sorted(away_match_played.items(), key=operator.itemgetter(1), reverse=True)

    return (home_match_played, away_match_played)

def top_ten(dict_list):
    topTen = {}
    sorted_dict = sorted(dict_list.items(), key=operator.itemgetter(1), reverse=True)

    for key, value in sorted_dict:
        topTen[key] = value
        if len(topTen) is 10:
            break
    return topTen


def sort_dict_by_value(dict_list):
    sorted_dict_list = {}

    sorted_list = sorted(dict_list.items(), key=operator.itemgetter(1), reverse=False)

    for key, value in sorted_list:
        sorted_dict_list[key] = value
    return sorted_dict



def top_ten_home_away_team(home_match_played, away_match_played):
    '''
    Following function takes two dictionaries as input,
    produces two dictionaries of top 10 home and away teams
    who played the most matches. Both results are sorted by
    values in descending order. 
    '''
    
    home_team = {}
    away_team = {}

    for team, quantity in home_match_played:
        home_team[team] = quantity
        if len(home_team) is 10:
            break

    for team, quantity in away_match_played:
        away_team[team] = quantity
        if len(away_team) is 10:
            break
    '''
    # Sort the dictionary by values in descending order
    home_team = sorted(home_team.items(), key=operator.itemgetter(1), reverse=True)
    away_team = sorted(away_team.items(), key=operator.itemgetter(1), reverse=True)
    '''
    return (home_team, away_team)



def plot_bar_graph(home_team):
    h_team_names = list(home_team.keys())
    h_team_values = list(home_team.values())
    plt.bar(range(len(home_team)), h_team_values, tick_label=h_team_names)
    plt.show()



def total_match_played(all_teams):
    
    total_match_played = {}

    for teams in all_teams:
        for team, quantity in teams:
            if team not in total_match_played.keys():
                total_match_played[team] = quantity
            else:
                total_match_played[team] = total_match_played[team] + quantity
    return total_match_played
