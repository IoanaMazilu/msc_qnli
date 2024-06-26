runs_innings_premise = 8
runs_innings_hypothesis = 5

# the hypothesis refers to the number of innings in which Suraj has runs, also mentioned in the premise
if runs_innings_hypothesis <= runs_innings_premise:
    # check if the estimate of 'runs_innings_hypothesis' contradicts the number of innings in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than 'runs_innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
