stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the time it takes Jim to stretch, which is also mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the estimate of'stretch_time_premise' contradicts the time in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
