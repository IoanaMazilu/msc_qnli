travel_distance_premise = 240
travel_distance_hypothesis = 340

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, mentioned in the premise
if travel_distance_hypothesis!= travel_distance_premise:
    # check if the distance traveled in the hypothesis contradicts the distance traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
