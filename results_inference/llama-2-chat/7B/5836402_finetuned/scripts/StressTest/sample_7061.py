dan_arrival_premise = 90
dan_arrival_hypothesis = 80

# the hypothesis refers to the arrival time of Dan in City A, also mentioned in the premise
if dan_arrival_hypothesis!= dan_arrival_premise:
    # check if the arrival time in the hypothesis contradicts the arrival time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
