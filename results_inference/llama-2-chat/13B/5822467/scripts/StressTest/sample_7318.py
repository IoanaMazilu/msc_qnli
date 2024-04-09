jim_stretch_premise = 78
jim_stretch_hypothesis = 18
cara_run_premise = 15

# the hypothesis refers to the time it takes Jim to stretch and the time Cara runs
if jim_stretch_hypothesis <= jim_stretch_premise:
    # check if the estimate of 'jim_stretch_hypothesis' contradicts the time it takes Jim to stretch in the premise
    label = "contradiction"
elif cara_run_premise!= cara_run_hypothesis:
    # check if the number of minutes Cara runs in the hypothesis contradicts the number of minutes Cara runs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
