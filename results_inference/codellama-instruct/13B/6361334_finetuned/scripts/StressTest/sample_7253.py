average_runs_premise = 8
average_runs_hypothesis = 4

# the hypothesis refers to the number of innings mentioned in the premise
if average_runs_hypothesis <= average_runs_premise:
    # check if the estimate of 'average_runs_hypothesis' contradicts the number of innings in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than 'average_runs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
