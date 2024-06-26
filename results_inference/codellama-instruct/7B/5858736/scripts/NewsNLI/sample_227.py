wickets_premise = 6
wickets_hypothesis = 6
runs_needed_premise = 150
runs_needed_hypothesis = 150

if wickets_hypothesis!= wickets_premise:
    # check if the number of wickets in the hypothesis contradicts the number of wickets in the premise
    label = "contradiction"
elif runs_needed_hypothesis!= runs_needed_premise:
    # check if the number of runs needed in the hypothesis contradicts the number of runs needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
