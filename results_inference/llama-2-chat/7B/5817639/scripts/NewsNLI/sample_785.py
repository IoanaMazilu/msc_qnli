# Define variables for premise and hypothesis
premise_teams = 0
hypothesis_teams = 0

# Extract quantities from premise and hypothesis
premise_teams = int(premise.split()[1])
hypothesis_teams = int(hypothesis.split()[1])

# Compare quantities
if hypothesis_teams!= premise_teams:
    # If the number of teams in the hypothesis contradicts the number of teams in the premise
    label = "contradiction"
elif hypothesis_teams < premise_teams:
    # If the number of teams in the hypothesis is less than the number of teams in the premise
    label = "entailment"
else:
    # If the number of teams in the hypothesis is the same as the number of teams in the premise
    label = "neutral"

# Print the label
print(label)
