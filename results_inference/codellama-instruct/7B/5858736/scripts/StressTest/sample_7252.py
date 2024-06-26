# Define variables for the numerical entities in the premise and hypothesis
runs_average_premise = 5
innings_premise = 8

# Check if the hypothesis value contradicts the estimate of more than 'runs_average_premise'
if innings_hypothesis <= runs_average_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than 'innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
