distance_premise = 40.0
speed_premise = 8.0
time_hypothesis = 5.0

# the hypothesis refers to the time Heather bicycled, which is related to the distance and speed in the premise
# compute the time Heather bicycled in the premise
time_premise = distance_premise / speed_premise
if time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
