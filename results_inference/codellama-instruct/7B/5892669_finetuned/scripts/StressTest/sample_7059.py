dan_leave_time_premise = 90
dan_leave_time_hypothesis = 20

# the hypothesis refers to the time Dan leaves City A after Cara, mentioned in the premise
if dan_leave_time_premise <= dan_leave_time_hypothesis:
    # check if the estimate of 'dan_leave_time_hypothesis' contradicts the time Dan leaves City A in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
