"""A collection of function for doing my project."""

import pandas as pd
import random

"""
Function: 
Removes any '*' characters from a string.
Teams in tables from https://www.basketball-reference.com/ have a * in their names to denote as playoff team.

----------
Parameters:
input_string: string
    string that may have a '*' in it

----------
Returns:
output_string: string
    modified string that should not contain any '*'

"""
def remove_star(input_string):
    if '*' in input_string:
        output_string = input_string.replace('*','')
    else:
        output_string = input_string
    return output_string



"""
Function:
Turns an input string into one that gets rid of the unnecessary word 'the' and removing any unnecessary white
space as well as capitalizing the first letter of every word in the string.

----------
Parameters:
input_string: string
    String, to be modified.
    
----------
Returns:
new_string: string
    Result of modification.
    

"""
def standardize_team(input_string):
    new_string = input_string.lower()
    
    #'Philadelphia 76ers' would be standardized to 'Philadelphia 76Ers'
    if 'philadelphia 76ers' in new_string:
        return 'Philadelphia 76ers'
    
    #'Seattle SuperSonics' would be standardized to 'Seattle Supersonics'
    if 'seattle supersonics' in new_string:
        return 'Seattle SuperSonics'
    
    #Removes any unnecessary white space
    new_string = new_string.strip()
    
    #Removes 'the' from the string
    new_string = new_string.replace('the ','')
    
    #Capitalizes the first letter in every word in the string
    new_string = new_string.title()
    return new_string



"""
Function:
Asks user to enter a certain year using the keyboard, and reads a csv based on that year.

----------
Parameters:
test: string
    Optional parameter, used for testing purposes
msg: string
    Based on used keyboard input
    
----------
Returns:
year: string
    Based on user input
df: DataFrame
    Dataframe from converted csv file. 'Team' column modified with remove_star function
    
"""
def year_input(test = None): 
    if not test:
        
        #When invalid_input is False, user inputs are considered valid
        invalid_input = True
        while invalid_input:
            
            #Takes in user input
            msg = input('YEAR :\t')
            year = msg
            
            #If the input passed can be created into a year, it is checked if it is a valid year between 1950 and 2018
            if year.isdigit() == True: 
                if int(year) >= 1950 and int(year) <= 2018:    
                    year = str(year)
                    
                    #Reads CSV based on year
                    filepath = 'my_module/BBallCSV/' + year + '.csv'
                    df = pd.read_csv(filepath)  
                    
                    #Applies remove_star function to 'Team' column
                    df['Team'] = df['Team'].apply(remove_star) 
                    invalid_input = False
                else:
                    #Error Statement
                    print('Invalid year! Please enter another year.')
            else:
                print('Invalid year! Please enter another year.')
        return year, df
    
    #For testing purposes
    else:
        df = pd.read_csv('BBallCSV/' + test + '.csv')      
        df['Team'] = df['Team'].apply(remove_star)       
        year = test
        return year, df
    
    
    
"""
Function:
Asks user to enter a certain team name using the keyboard, and reads the passed dataframe based on that team name. 
Creates a new dataframe that holds the info of one NBA team, with an additional 'year' column that holds the year
that team is from. Prints possible team names if keyboard input is 'Team'.

----------
Parameters:
year: string
    To be added to a newly created dataframe under a new 'year' column
df: DataFrame
    DataFrame to be read by function
test: string
    Optional parameter, for testing purposes only 
    
----------
Returns:
team: string
    Based on keyboard input that has been modified by standardize_team
df_team: DataFrame
    Trimmed dataframe that holds the info of only one team and contains a new 'year' column which has a value 
    based on the passed 'year' parameter.
    
"""
def team_input(year, df, test = None):
    if not test:
        
        #If user inputs are valid, invalid_input will be False
        invalid_input = True
        while invalid_input:   
            
            #User keyboard input
            msg = input('TEAM :\t')
            
            #Applies standardize_team function to User Keyboard Input
            msg = standardize_team(msg)
            
            #If the message is 'Team', valid team names are printed in alphabetical order
            if msg == 'Team':
                df = df.sort_values(by=['Team'])
                print(df['Team'].to_string(index=False))
            
            #Error message
            elif msg not in df['Team'].values:
                print('Invalid Team! Please enter another team.')
            
            #Valid team name, searches df for team and copies it into a new dataframe containing info for that team only
            #Adds a new 'year' column to the new dataframe based on year passed
            else:
                team = msg
                df_team = df.loc[df['Team'] == msg]
                df_year = pd.DataFrame({'year': [year]})
                df_team = pd.concat([df_team, df_year], axis=1)
                invalid_input = False
        return team, df_team
    
    #For testing purposes
    else:
        msg = test
        msg = standardize_team(msg)
        team = msg
        df_team = df.loc[df['Team'] == msg]
        df_year = pd.DataFrame({'year': [year]})
        df_team = pd.concat([df_team, df_year], axis=1)
        return team, df_team
    
    
    
"""
Function:
Checks if team strings and year strings are equal to each other. Prints an error message if both teams are 
the same and are from the same year.

----------
Parameters:
first_team_year, second_team_year: string
    Strings that are to be checked for identicality
first_team, second_team: string
    Strings that are to be checked for Identicality
    
----------
Returns:
Boolean: True or False
    
"""
def check_teams(first_team_year, second_team_year, first_team, second_team):
    
    #Checks if the two teams are from the same year and the same team, returns True and prints message if they are the same
    if first_team == second_team and first_team_year == second_team_year:
        print("These two teams are the same! Please choose different teams.")
        return True
    else:
        return False
    
    
    
"""
Function:
Appends two dataframes and removes unnecessary columns. Sets the team names as the index of the appended dataframe.
If the two team names are the same it sets the year column as the index.

----------
Parameters:
first_team, second_team: string
    Year strings can also be passed. Used to compare similarity if the index should be based on team name or year.
df_first_team, df_second_team: DataFrame
    Dataframes to be combined into one dataframe and have indexes set based on team or year 
    if the team names are the same
----------
Returns:
df_appended: DataFrame
    Appended dataframe of df_first_team and df_second_team.
    
"""
def append_and_drop(first_team, df_first_team, second_team, df_second_team):
    
    #If the two team names are the same, the 'team' column is dropped.
    if first_team == second_team:
        df_first_team = df_first_team.drop(['Team'], axis = 1)
        df_second_team = df_second_team.drop(['Team'], axis = 1)

    #Appends the two dataframes
    df_appended = df_first_team.append(df_second_team, ignore_index = True)
        
    #Drops irrelevant columns, sets index to 'year' column if teams are the same, else the team column becomes the index for the new dataframe
    if first_team == second_team:
        df_appended = df_appended.drop(['Rk','G','MP','FG','FGA','3P','3PA','2P','2PA','FT','FTA','TOV'], axis = 1)
        df_appended = df_appended.set_index('year')
    else:  
        df_appended = df_appended.drop(['Rk','G','MP','FG','FGA','3P','3PA','2P','2PA','FT','FTA','TOV','year'], axis = 1)
        df_appended = df_appended.set_index('Team')
    
    return df_appended
        

    
"""
Function:
Analyzes a dataframe and compares the values in certain columns. If a team has a higher value than another team 
in a column, that team gets one point added to their score variable.

----------
Parameters:
first_team, second_team: string
    Index values of dataframe, can also be years if both teams passed were the same but different years.
df: DataFrame
    DataFrame to be searched.
----------
Returns:
return_int: int 
    Result of the scores between both teams subtracted from each other
"""
def calculate_score(df, first_team, second_team):
    #Scores between two teams to be calculated
    first_team_score = 0
    second_team_score = 0
    
    #Column names of the DataFrame
    index_list = list(df)
    
    for index in index_list:
        #If a value is Null or both values are the same, the column is skipped and is not considered part of the calculation.
        if pd.isnull(df.at[first_team, index]):
            continue
        elif pd.isnull(df.at[second_team, index]):
            continue
        elif df.at[first_team, index] == df.at[second_team, index]:
            continue
        
        #Adds a point to the team_score variables if one team has a higher value than the other
        elif df.at[first_team, index] > df.at[second_team, index]:
            first_team_score += 1
        elif df.at[first_team, index] < df.at[second_team, index]:
            second_team_score += 1
    
    #Result of having the first_team_score and second_team_score subtracted from each other
    return_int = first_team_score - second_team_score
    return return_int



"""
Function:
Analyzes a dataframe and compares the values in certain columns. If a team has a higher value than another team 
in a column, that team gets one point added to their score variable.

----------
Parameters:
df_appended: DataFrame
    DataFrame to be searched.
first_team, first_team_year, second_team, second_team_year: string
    Teams are considered index values of df_appended but if team names are the same (but different years), years are considered as the index values
    
----------
Returns:
final_score: int 
    Result of the scores between both teams subtracted from each other
"""
def check_calculate_score(df_appended, first_team, first_team_year, second_team, second_team_year):
    
    #Calculates score, checks if team names are the same. 
    #If they are, years are considered the index values, otherwise team names are index values.
    if first_team == second_team:
        final_score = calculate_score(df_appended, first_team_year, second_team_year)
    else:
        final_score = calculate_score(df_appended, first_team, second_team)
    return final_score



"""
Function:
Analyzes the score variable passed and returns a string message based on the score. If the score is 0, winner is determined by a coin flip.

----------
Parameters:
score: int
    To be passed and analyzed by the function.
first_team, second_team: string
    Strings that hold team names
first_team_year, second_team_year: float 
    int that hold the year the teams are from
----------
Returns:
return_string: string
    String that holds the bot message for the prediction

"""
def calculate_prediction(score, first_team, first_team_year, second_team, second_team_year):
    
    #Converts float to string
    first_team_year = str(first_team_year)
    second_team_year = str(second_team_year)
    
    #Checks score and returns relevant message string. Positive scores mean team 1 wins while negative scores mean team 2 wins
    #How far away the score is from 0 represents how many games the seven game series will take
    if score <= 12 and score >= 9:
        return_string = "This is a wrap. I predict the " + first_team_year + " " + first_team + " will win versus the " + second_team_year + " " + second_team + " in 4 games."
    elif score <= 8 and score >= 5:
        return_string = "This is a pretty easy decision. I predict the " + first_team_year + " " + first_team + " will win versus the " + second_team_year + " " + second_team + " in 5 games."
    elif score <= 4 and score >= 1:
        return_string = "This is tough, but I predict the " + first_team_year + " " + first_team + " will win versus the " + second_team_year + " " + second_team + " in 6 games."
    
    #If the score is 0, a coin flip is used to determine the winner
    elif score == 0:
        coin = random.randint(0, 1)
        if coin == 0:
            return_string = "This is a difficult decision. Both of these teams are so evenly but I predict that the " + first_team_year + " " + first_team + " will beat the " + second_team_year + " " + second_team + " in 7 games!"
        elif coin == 1:
            return_string = "This is a difficult decision. Both of these teams are so evenly but I predict that the " + second_team_year + " " + second_team + " will beat the " + first_team_year + " " + first_team + " in 7 games!"
    
    elif score >= -12 and score <= -9:
        return_string = "This is a wrap. I predict the " + second_team_year + " " + second_team + " will win versus the " + first_team_year + " " + first_team + " in 4 games."
    elif score >= -8 and score <= -5:
        return_string = "This is a pretty easy decision. I predict the " + second_team_year + " " + second_team + " will win versus the " + first_team_year + " " + first_team + " in 5 games."
    elif score >= -4 and score <= -1:
        return_string = "This is tough, but I predict the " + second_team_year + " " + second_team + " will win versus the " + first_team_year + " " + first_team + " in 6 games."
    return return_string