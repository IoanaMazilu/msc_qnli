dan_hours_premise = 8
dan_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works alone
if dan_hours_premise <= dan_hours_hypothesis:
    # check if the estimate of 'dan_hours_hypothesis' contradicts the number of hours Dan works alone in the premise
    label = "contradiction"
elif dan_hours_hypothesis!= annie_hours_premise:
    # check if the number of hours Annie needs to complete the job in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
