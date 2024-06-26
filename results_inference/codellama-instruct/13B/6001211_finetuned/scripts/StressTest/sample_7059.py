dan_leaving_time_premise = 90
dan_leaving_time_hypothesis = 20

# the hypothesis refers to the time Dan leaves City A after Cara, mentioned in the premise
if dan_leaving_time_premise <= dan_leaving_time_hypothesis:
    # check if the estimate of 'dan_leaving_time_hypothesis' contradicts the time Dan leaves after Cara in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
