stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the time it takes Jim to stretch, which is also mentioned in the premise
if stretch_time_hypothesis < stretch_time_premise:
    # check if the estimate of'stretch_time_hypothesis' contradicts the time it takes Jim to stretch in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
