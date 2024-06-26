travel_distance_premise = 240
travel_distance_hypothesis = 440

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, mentioned in the premise
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the distance traveled in the premise contradicts the estimate of less than 'travel_distance_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
