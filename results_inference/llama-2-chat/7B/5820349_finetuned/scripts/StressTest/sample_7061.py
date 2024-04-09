dan_leave_time_premise = 90
dan_leave_time_hypothesis = 80

# the hypothesis refers to the time Dan leaves City A after Cara, also mentioned in the premise
if dan_leave_time_hypothesis!= dan_leave_time_premise:
    # check if the time Dan leaves in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
