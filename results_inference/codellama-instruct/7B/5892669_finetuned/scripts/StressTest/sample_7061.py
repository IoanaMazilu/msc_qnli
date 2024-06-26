dan_leave_time_premise = 90
dan_leave_time_hypothesis = 80

# the hypothesis refers to the time Dan leaves City A after Cara, mentioned in the premise
if dan_leave_time_hypothesis!= dan_leave_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
