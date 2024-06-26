distance_premise = 25.0
speed_premise = 5.0
time_hypothesis = 4.0

# the hypothesis refers to the time taken to jog, which is also mentioned in the premise
# compute the distance jogged in the premise
distance_premise = distance_premise / speed_premise
if distance_premise!= time_hypothesis:
    # check if the time taken to jog in the hypothesis contradicts the time taken to jog from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
