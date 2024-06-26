distance_premise = 40.0
speed_premise = 8.0
time_hypothesis = 3.0

# the hypothesis refers to the time bicycled, which can be calculated from the premise
# compute the time bicycled in the premise
time_premise = distance_premise / speed_premise
if time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
