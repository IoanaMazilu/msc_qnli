# Define variables for the numerical entities in the premise and hypothesis
premise_halftime_score = 3
premise_away_team = "West Bromwich Albion"
premise_draw = 3

hypothesis_second_half_goals = 3
hypothesis_draw = 3

# Extract all quantities as valid numbers
premise_halftime_score = float(premise_halftime_score)
premise_away_team = str(premise_away_team)
premise_draw = float(premise_draw)

hypothesis_second_half_goals = float(hypothesis_second_half_goals)
hypothesis_draw = float(hypothesis_draw)

# Use brief comments to explain what comparison you do between the defined variables
if premise_halftime_score!= hypothesis_second_half_goals:
    # Check if the halftime score in the hypothesis contradicts the halftime score in the premise
    label = "contradiction"
elif premise_away_team!= hypothesis_away_team:
    # Check if the away team in the hypothesis contradicts the away team in the premise
    label = "contradiction"
elif premise_draw!= hypothesis_draw:
    # Check if the draw in the hypothesis contradicts the draw in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
