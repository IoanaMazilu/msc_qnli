# Define variables for the numerical entities in the premise and hypothesis
goals_premise = 2
goals_hypothesis = 0

# Extract all quantities as valid numbers
goals_premise = float(goals_premise)
goals_hypothesis = float(goals_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if goals_hypothesis!= goals_premise:
    # Check if the number of goals scored by Slovenia in the hypothesis contradicts the number of goals scored by the United States in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
