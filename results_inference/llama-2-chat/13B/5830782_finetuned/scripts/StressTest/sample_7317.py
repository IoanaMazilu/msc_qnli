stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the stretching time mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the estimate of'stretch_time_hypothesis' contradicts the stretching time in the premise
    label = "contradiction"
elif stretch_time_premise < stretch_time_hypothesis:
    # if the stretching time in the premise is less than the stretching time in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
