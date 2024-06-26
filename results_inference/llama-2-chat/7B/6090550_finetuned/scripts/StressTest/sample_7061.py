dan_leave_premise = 90
dan_leave_hypothesis = 80

# the hypothesis refers to the time Dan leaves City A after Cara, which is also mentioned in the premise
if dan_leave_hypothesis!= dan_leave_premise:
    # check if the time Dan leaves City A in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
