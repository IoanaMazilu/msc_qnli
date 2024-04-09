dan_leave_time_premise = 90
dan_leave_time_hypothesis = 20

# the hypothesis refers to the time difference between Dan and Cara leaving City A
if dan_leave_time_premise <= dan_leave_time_hypothesis:
    # check if the estimate of 'dan_leave_time_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
