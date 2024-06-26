stretch_premise = 10
stretch_hypothesis = 60

# the hypothesis refers to the time at which Pat stops stretching
if stretch_hypothesis <= stretch_premise:
    # check if the estimate of'stretch_hypothesis' contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
