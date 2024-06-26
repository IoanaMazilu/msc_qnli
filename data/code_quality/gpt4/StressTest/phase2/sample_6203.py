travel_distance_premise = 200
travel_distance_hypothesis = 200

# the hypothesis talks about the distance Louisa traveled on her vacation, which is also referenced in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the exact distance of 'travel_distance_premise' miles
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
