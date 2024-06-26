average_runs_premise = 8
average_runs_hypothesis = 4

# the hypothesis refers to the number of runs Suraj has in a certain number of innings, which is also mentioned in the premise
if average_runs_hypothesis <= average_runs_premise:
    # check if the hypothesis value contradicts the estimate of 'average_runs_premise'
    label = "contradiction"
elif average_runs_hypothesis > average_runs_premise:
    # if the hypothesis value is greater than the premise value, it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
