dan_leaving_time_premise = 90
dan_leaving_time_hypothesis = 80

# the hypothesis refers to the time Dan leaves City A after Cara, which is also mentioned in the premise
if dan_leaving_time_hypothesis!= dan_leaving_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
