travel_distance_premise = 100
travel_distance_hypothesis = 600

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, which is also mentioned in the premise
if travel_distance_hypothesis != travel_distance_premise:
    # check if the hypothesized travel distance contradicts the travel distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, then we have entailment
    label = "entailment"

print(label)
