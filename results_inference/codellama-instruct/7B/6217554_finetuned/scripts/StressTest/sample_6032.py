distance_traveled_premise = 1/2
distance_traveled_hypothesis = 7/2

# the hypothesis talks about the distance traveled by Maria, referenced also in the premise
if distance_traveled_hypothesis!= distance_traveled_premise:
    # check if the distance traveled in the hypothesis contradicts the distance traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)