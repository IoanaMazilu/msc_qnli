distance_premise = 40.0
speed_premise = 8.0
time_hypothesis = 5.0

# the hypothesis refers to the time Heather bicycled, which is also mentioned in the premise
if time_hypothesis!= distance_premise / speed_premise:
    # check if the time from the hypothesis contradicts the time estimated from the distance and speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
