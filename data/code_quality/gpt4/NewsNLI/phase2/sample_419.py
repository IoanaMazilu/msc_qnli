distance_from_little_rock_premise = 37
distance_from_little_rock_hypothesis = 37

# the hypothesis mentions the distance of the quake's epicenter from Little Rock, which is also mentioned in the premise
if distance_from_little_rock_hypothesis != distance_from_little_rock_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance from the hypothesis does not contradict the premise distance, we can infer entailment
    label = "entailment"

print(label)
