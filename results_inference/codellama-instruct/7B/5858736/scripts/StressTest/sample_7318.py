jim_stretch_premise = 78
jim_stretch_hypothesis = 18
cara_run_premise = 1

# the hypothesis refers to the time it takes Jim to stretch and the time Cara continues to run
if jim_stretch_hypothesis <= jim_stretch_premise:
    # check if the estimate of 'jim_stretch_hypothesis' contradicts the time it takes Jim to stretch in the premise
    label = "contradiction"
elif cara_run_premise!= 1:
    # check if the number of minutes Cara continues to run in the hypothesis contradicts the time it takes Cara to run in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
