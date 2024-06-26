leave_time_premise = 120
leave_time_hypothesis = 520

# the hypothesis refers to the time Dan leaves City A after Cara, also mentioned in the premise
if leave_time_hypothesis < leave_time_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
elif leave_time_premise > leave_time_hypothesis:
    # check if the time reported in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
