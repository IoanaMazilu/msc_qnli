distance_premise = 40.0
speed_premise = 8.0
time_hypothesis = 3.0

# the hypothesis refers to the time spent bicycling, which is also mentioned in the premise
# compute the distance traveled based on the speed and time
distance_hypothesis = speed_premise * time_hypothesis
if distance_hypothesis!= distance_premise:
    # check if the distance traveled in the hypothesis contradicts the distance from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
