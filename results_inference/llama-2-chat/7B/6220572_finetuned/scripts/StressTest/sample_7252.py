runs_innings_premise = 5
runs_innings_hypothesis = 8

# the hypothesis refers to the number of innings in which Suraj's average of runs is computed
if runs_innings_hypothesis <= runs_innings_premise:
    # check if the hypothesis estimate contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than 'runs_innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
