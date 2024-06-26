dan_leave_time_premise = 120
dan_leave_time_hypothesis = 520

# the hypothesis refers to the time Dan leaves City A after Cara, mentioned in the premise
if dan_leave_time_hypothesis < dan_leave_time_premise:
    # check if the estimate of 'dan_leave_time_hypothesis' contradicts the time Dan leaves City A in the premise
    label = "contradiction"
elif dan_leave_time_hypothesis > dan_leave_time_premise:
    # check if the time Dan leaves City A in the hypothesis is more than the time reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
