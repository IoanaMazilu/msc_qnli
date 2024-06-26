runs_per_innings_premise = 8
runs_per_innings_hypothesis = 4

# the hypothesis refers to the average number of runs per innings of Suraj, also mentioned in the premise
if runs_per_innings_hypothesis!= runs_per_innings_premise:
    # check if the average number of runs per innings in the hypothesis contradicts the average number of runs per innings in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
