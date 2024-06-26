travel_distance_premise = 200
travel_distance_hypothesis = 200

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, mentioned in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the exact distance traveled as per the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
