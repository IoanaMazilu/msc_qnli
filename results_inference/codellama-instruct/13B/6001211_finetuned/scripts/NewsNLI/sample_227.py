needed_runs_premise = 150
trailing_runs_hypothesis = 150
wickets_left_premise = 6
wickets_left_hypothesis = 6

# the hypothesis mentions the number of runs needed and the wickets left, which are also mentioned in the premise
if trailing_runs_hypothesis!= needed_runs_premise:
    # check if the trailing runs in the hypothesis contradicts the needed runs reported in the premise
    label = "contradiction"
elif wickets_left_hypothesis!= wickets_left_premise:
    # check if the number of wickets left from the hypothesis contradicts the number of wickets left in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
