stretch_time_premise = 18
stretch_time_hypothesis = 18

# the hypothesis refers to the stretching time of Jim mentioned in the premise
if stretch_time_hypothesis > stretch_time_premise:
    # check if the hypothesis value contradicts the stretching time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
