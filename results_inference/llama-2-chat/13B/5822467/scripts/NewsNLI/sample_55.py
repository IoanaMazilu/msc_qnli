premise_games = 3
hypothesis_games = 3

# define variables with representative names for the numerical entities in both inputs
games_premise = premise_games
games_hypothesis = hypothesis_games

# extract all quantities as valid numbers (integers or floats)
games_premise = int(games_premise)
games_hypothesis = int(games_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# check if the number of games in the hypothesis contradicts the number of games in the premise
if games_hypothesis!= games_premise:
    # if the number of games in the hypothesis contradicts the number of games in the premise, the hypothesis contradicts the premise
    label = "contradiction"

# if the number of games in the hypothesis does not contradict the number of games in the premise, we can infer neutrality
else:
    label = "neutral"

print(label)
