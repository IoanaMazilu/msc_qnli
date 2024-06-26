premise = "Amanda goes to the toy store to buy less than 6 ball and 3 different board games."
hypothesis = "Amanda goes to the toy store to buy 1 ball and 3 different board games."

# extract the numerical entities from the premise
premise_ball = 6
premise_board_games = 3

# extract the numerical entities from the hypothesis
hypothesis_ball = 1
hypothesis_board_games = 3

# check if the hypothesis value contradicts the premise estimate
if hypothesis_ball > premise_ball:
    label = "contradiction"
elif hypothesis_board_games!= premise_board_games:
    label = "contradiction"
else:
    label = "entailment"

print(label)
