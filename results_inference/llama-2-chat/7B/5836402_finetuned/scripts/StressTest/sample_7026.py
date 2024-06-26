dan_arrival_premise = 120
dan_arrival_hypothesis = 520

# the hypothesis refers to the time difference between Dan's arrival and Cara's arrival mentioned in the premise
if dan_arrival_hypothesis >= dan_arrival_premise:
    # check if the estimate of 'dan_arrival_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
elif dan_arrival_hypothesis < dan_arrival_premise:
    # check if the time difference in the hypothesis contradicts the time difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
