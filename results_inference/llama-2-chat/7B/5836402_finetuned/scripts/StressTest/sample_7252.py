average_runs_premise = 5
average_runs_hypothesis = 8
innings_hypothesis = 8

# the hypothesis refers to the number of innings, which is also mentioned in the premise
if average_runs_premise <= average_runs_hypothesis:
    # check if the estimate of 'average_runs_hypothesis' contradicts the number of runs in the premise
    label = "contradiction"
elif innings_hypothesis!= average_runs_premise:
    # check if the number of innings in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
