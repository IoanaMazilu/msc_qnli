travel_distance_premise = 200
travel_distance_hypothesis = 300

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the distance traveled in the premise contradicts the estimate of less than 'travel_distance_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
