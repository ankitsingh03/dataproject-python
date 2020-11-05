# IPL Data Set Analytics

## Aim

To convert raw open data (run by run records in this case) into charts that tell some kind of story.

## How To Get The Data.

To download the data [click here](https://www.kaggle.com/manasgarg/ipl/version/5). Here you will get two data files.
Third data file is present in project itself.

## Install Package Dependency.
In project **requirement.txt** file is present. It has all the list of packages which is needed to run the project. Run this command to install all the required package `pip install -r requirement.txt`

## How To Run
There are four problems Statement in this. so, run charts one by one.
#### Problem 1: Total runs scored by team
- Plot a chart of the total runs scored by each teams over the history of IPL. Hint: use the total_runs field.
- To see the graph. Run this command in project directory  `python3 total_run_scored_by_team.py`

#### Problem 2: Top batsman for Royal Challengers Bangalore
- Consider only games played by Royal Challengers Bangalore. Now plot the total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.
- To see the graph. Run this command in project directory `python3 top_batsman_for_royal_challengers_bangalore.py`

#### Problem 3: Foreign umpire analysis
- Obtain a source for country of origin of umpires. Plot a chart of number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph.
- To see the graph. Run this command in project directory `python3 foreign_umpire_analysis.py`

#### Problem 4: Stacked chart of matches played by team by season

- Plot a stacked bar chart of :
- Number of games played
- By team
- By season

- To see the graph. Run this command in project directory `python3 stacked_chart_of_matches_played_by_team_by_season.py` 