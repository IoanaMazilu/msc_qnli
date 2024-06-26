distance_walked_premise = 4.0
speed_premise = 3.0
time_walked_hypothesis = 2.9

# the hypothesis refers to the time walked, which can be computed from the premise
# compute the time walked in the premise
time_walked_premise = distance_walked_premise / speed_premise
if time_walked_hypothesis!= time_walked_premise:
    # check if the time walked in the hypothesis contradicts the time walked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
