# Define variables with representative names for the numerical entities in both inputs
premise_goals = 4
premise_goals_scored = 2
hypothesis_goals = 4
hypothesis_goals_scored = 2

# Extract all quantities as valid numbers (integers or floats)
premise_goals = int(premise_goals)
premise_goals_scored = int(premise_goals_scored)
hypothesis_goals = int(hypothesis_goals)
hypothesis_goals_scored = int(hypothesis_goals_scored)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_goals!= premise_goals:
    # Check if the number of goals in the hypothesis contradicts the number of goals in the premise
    label = "contradiction"
elif hypothesis_goals_scored!= premise_goals_scored:
    # Check if the number of goals scored in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
