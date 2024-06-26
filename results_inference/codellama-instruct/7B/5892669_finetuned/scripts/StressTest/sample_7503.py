stretch_time_premise = 10
stretch_time_hypothesis = 20

# the hypothesis refers to the time when Pat stops to stretch, mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the estimate of'stretch_time_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
