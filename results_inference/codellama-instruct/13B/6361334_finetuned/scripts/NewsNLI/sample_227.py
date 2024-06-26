runs_premise = 150
runs_hypothesis = 150
wickets_premise = 6
wickets_hypothesis = 6

# the hypothesis mentions the number of runs and wickets left, which are also mentioned in the premise
if runs_hypothesis!= runs_premise:
    # check if the number of runs from the hypothesis contradicts the number of runs in the premise
    label = "contradiction"
elif wickets_hypothesis!= wickets_premise:
    # check if the number of wickets from the hypothesis contradicts the number of wickets in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
