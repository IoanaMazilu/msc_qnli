distance_premise = 48
distance_hypothesis = 18

# the hypothesis refers to the distance between Lionel's house and Walt's house mentioned in the premise
if distance_premise < distance_hypothesis:
    # check if the distance in the premise contradicts the estimation of more than 'distance_hypothesis' miles
    label = "contradiction"
elif distance_premise == distance_hypothesis:
    # check if the distance in the premise contradicts the estimation of more than 'distance_hypothesis' miles
    label = "contradiction"
else:
    # if the distance in the premise does not contradict the estimation in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
