# Dallin Moore
# HW5

import requests
import json
import os
from statistics import mean

# function to display the string when it's printed
def format_date(date):
    date_str = str(date)
    formatted_date = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:]}" if len(date_str) == 8 else f"{date_str[0:4]}-{date_str[4:6]}"
    return formatted_date

# get the current directory of this file
curr_dir = os.path.dirname(__file__) 

# build a list of the state abbreviation to access
file_path = curr_dir + '/' + 'states_territories.txt'
# Open the file and read lines into a list
with open(file_path, 'r') as file:
    states_territories = [line.strip() for line in file.readlines()]

# build a list of the state names to access
file_path = curr_dir + '/' + 'states_territories_name.txt'
# Open the file and read lines into a list
with open(file_path, 'r') as file:
    states_territories_names = [line.strip() for line in file.readlines()]

# keys
new_cases_key='positiveIncrease'
date_key='date'

# loop through all of the states/territories
for state in states_territories:
    
    # access all of the API's data for the state
    url = f"https://api.covidtracking.com/v1/states/{state}/daily.json"
    request = requests.get(url)
    days_results = json.loads(request.text)
    
    # save the dictionary to a file
    state_file_path = curr_dir + "/state_results/" + state.upper() + ".json"
    with open(state_file_path, "w") as file:
        json.dump(days_results, file, indent=2)
    
    # initialize variables
    new_daily_cases = []
    dates = []
    monthly_cases = {}
    
    # loop through each day of the json
    for day in days_results:
        new_case = day[new_cases_key]
        date = day[date_key]
        new_daily_cases.append(new_case)
        dates.append(date)
        month_key = date // 100 # eliminate the day from the date
        monthly_cases[month_key] = monthly_cases.get(month_key, 0) + new_case
    
    # print the same info from the dictionary
    print('State name:',states_territories_names[states_territories.index(state)])
    print('Average number of new daily cases:',mean(new_daily_cases))
    print('Date with the highest new number of cases:',format_date(dates[new_daily_cases.index(max(new_daily_cases))]))
    print('Most recent date with no new cases:',format_date( max([date for date, cases in list(zip(dates, new_daily_cases)) if cases == 0])))
    print('Month with the highest new number of cases:',format_date(max(monthly_cases, key=monthly_cases.get)))
    print('Month with the lowest new number of cases:',format_date(min(monthly_cases, key=monthly_cases.get)),'\n')
