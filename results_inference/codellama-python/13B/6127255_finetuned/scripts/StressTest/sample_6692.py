# air_travel_distance_premise = 1800
# air_travel_distance_hypothesis = 7800

# # the hypothesis refers to the same air travel distance mentioned in the premise
# if air_travel_distance_hypothesis!= air_travel_distance_premise:
#     # check if the air travel distance in the hypothesis contradicts the air travel distance reported in the premise
#     label = "contradiction"
else:
    # if the air travel distance in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
