"""Test for my functions. Some functions require the output of other functions
"""

import pandas as pd
import random
from functions import remove_star, standardize_team, year_input, team_input, check_teams, append_and_drop, calculate_score, check_calculate_score, calculate_prediction

def test_bballbot():
    assert callable(remove_star)
    assert remove_star('Golden State Warriors') == 'Golden State Warriors'
    assert remove_star('Golden State Warriors*') == 'Golden State Warriors'
    


    assert callable(standardize_team)
    assert standardize_team('the chicago bulls') == 'Chicago Bulls'
    assert standardize_team('CHICAGO BULLS') == 'Chicago Bulls'



    assert callable(year_input)
    a, b = year_input('2018')
    assert a == '2018'
    assert isinstance(b, pd.DataFrame)



    assert callable(team_input)
    c, d = team_input(a, b, 'Golden State Warriors')
    assert c == 'Golden State Warriors'
    assert isinstance(d, pd.DataFrame)


    assert callable(check_teams)
    a1, b1 = year_input('2017')
    c1, d1 = team_input(a1, b1, 'Chicago Bulls')
    assert check_teams(a,a,c,c) == True
    assert check_teams(a,a1,c,c1) == False



    assert callable(append_and_drop)
    e = append_and_drop(c, d, c1, d1)
    assert isinstance(e, pd.DataFrame)


    assert callable(calculate_score)
    f = calculate_score(e, c, c1)
    assert isinstance(f, int)


    assert callable(check_calculate_score)
    g = check_calculate_score(e, c, a, c1, a1)
    assert isinstance(g, int)

    assert callable(calculate_prediction)
    h = calculate_prediction(g, c, a, c1, a1)
    assert isinstance(h, str)
