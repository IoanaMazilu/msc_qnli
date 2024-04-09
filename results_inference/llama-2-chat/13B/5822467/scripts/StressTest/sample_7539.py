balls_premise = 1
board_games_premise = 3

# define variables with representative names for the numerical entities in both inputs
balls_hypothesis = -6

# extract all quantities as valid numbers (integers or floats)
balls_premise = int(balls_premise)
balls_hypothesis = int(balls_hypothesis)
board_games_premise = int(board_games_premise)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the number of balls in the hypothesis to the number of balls in the premise
if balls_hypothesis <= balls_premise:
    # check if the estimate of 'balls_hypothesis' contradicts the number of balls in the premise
    label = "contradiction"
elif balls_hypothesis > balls_premise:
    # check if the number of balls in the hypothesis is greater than the number of balls in the premise
    label = "entailment"
else:
    # the hypothesis value and the premise value are equal
    label = "neutral"

# compare the number of board games in the hypothesis to the number of board games in the premise
if board_games_hypothesis == board_games_premise:
    # check if the number of board games in the hypothesis is equal to the number of board games in the premise
    label = "neutral"
else:
    # the number of board games in the hypothesis is different from the number of board games in the premise
    label = "contradiction"

# use the correct comparison operators
# sometimes the textual information indicates neutrality and no comparison is needed

print(label)
