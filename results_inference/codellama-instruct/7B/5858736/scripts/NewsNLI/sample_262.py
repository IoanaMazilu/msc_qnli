# Define variables with representative names for the numerical entities in both inputs
goals_premise = 6
goals_hypothesis = 6

# Extract all quantities as valid numbers (integers or floats)
goals_premise = int(goals_premise)
goals_hypothesis = int(goals_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if goals_hypothesis!= goals_premise:
    # Check if the number of goals scored by Napoli in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
