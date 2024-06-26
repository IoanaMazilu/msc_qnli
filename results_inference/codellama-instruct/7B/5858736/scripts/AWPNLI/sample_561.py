# Define variables for the numerical entities in the premise and hypothesis
birds_sitting_premise = 21.0
birds_flew_away_premise = 14.0
birds_left_hypothesis = 6.0

# Extract all quantities as valid numbers
total_birds_premise = birds_sitting_premise + birds_flew_away_premise

# Use brief comments to explain what comparison you do between the defined variables
if total_birds_premise - birds_left_hypothesis!= 0:
    # Check if the total number of birds in the premise is not equal to the number of birds left in the hypothesis
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
