premise = "If the toy store is stocked with 3 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?"
hypothesis = "If the toy store is stocked with less than 5 types of balls and 6 types of board games, how many different selections of the 4 items can Amanda make?"

# extract the numerical entities from the premise and hypothesis
premise_balls = 3
premise_board_games = 6
hypothesis_balls = 5
hypothesis_board_games = 6

# calculate the number of different selections of the 4 items
premise_selections = premise_balls * premise_board_games
hypothesis_selections = hypothesis_balls * hypothesis_board_games

# compare the number of selections in the premise and hypothesis
if premise_selections <= hypothesis_selections:
    label = "entailment"
elif premise_selections > hypothesis_selections:
    label = "contradiction"
else:
    label = "neutral"

print(label)
