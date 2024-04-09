runs_needed_premise = 150
runs_needed_hypothesis = 150
wickets_left_premise = 6
wickets_left_hypothesis = 6

# the hypothesis mentions the number of runs needed and the number of wickets left, which are also mentioned in the premise
if runs_needed_hypothesis!= runs_needed_premise:
    # check if the number of runs needed in the hypothesis contradicts the number of runs needed in the premise
    label = "contradiction"
elif wickets_left_hypothesis!= wickets_left_premise:
    # check if the number of wickets left from the hypothesis contradicts the number of wickets left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
