stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the stretching time of Jim mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the estimate of 'stretch_time_hypothesis' contradicts the actual stretching time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
