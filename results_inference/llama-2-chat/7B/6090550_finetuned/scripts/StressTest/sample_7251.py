average_runs_premise = 8
average_runs_hypothesis = 5

# the hypothesis refers to the average number of runs in a series of innings, which is also mentioned in the premise
if average_runs_hypothesis >= average_runs_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_runs_hypothesis < average_runs_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
