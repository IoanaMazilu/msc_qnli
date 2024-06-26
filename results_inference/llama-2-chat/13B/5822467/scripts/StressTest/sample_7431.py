balls_premise = 3
balls_hypothesis = float(input("Enter the number of ball types in the store (more than 1): "))
board_games_premise = 6
board_games_hypothesis = float(input("Enter the number of board game types in the store (more than 1): "))

# define variables for the premise and hypothesis
selections_premise = (balls_premise * board_games_premise)
selections_hypothesis = (balls_hypothesis * board_games_hypothesis)

# compare the premise and hypothesis values
if selections_premise <= selections_hypothesis:
    # the hypothesis value is less than or equal to the premise value, so there is no contradiction
    label = "neutral"
elif selections_hypothesis > selections_premise:
    # the hypothesis value is greater than the premise value, so there is entailment
    label = "entailment"
else:
    # the hypothesis value is less than the premise value, so there is contradiction
    label = "contradiction"

print(label)
