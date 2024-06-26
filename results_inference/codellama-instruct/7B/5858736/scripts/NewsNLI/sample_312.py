# Define variables with representative names for the numerical entities in both inputs
games_premise = 1
goals_premise = 4
teams_premise = 2

# Extract all quantities as valid numbers (integers or floats)
games_hypothesis = 1
goals_hypothesis = 4
teams_hypothesis = 2

# Use brief comments to explain what comparison you do between the defined variables
if goals_hypothesis!= goals_premise:
    # check if the number of goals scored by Danny Welbeck in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
elif teams_hypothesis!= teams_premise:
    # check if the number of teams involved in the hypothesis contradicts the number of teams involved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
