dan_leave_time_premise = 120
dan_leave_time_hypothesis = 120

# the hypothesis refers to the time Dan leaves City A, which is also mentioned in the premise
if dan_leave_time_hypothesis <= dan_leave_time_premise:
    # check if the hypothesis value contradicts the exact time 'dan_leave_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
