travel_distance_premise = 200
travel_distance_hypothesis = 300

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, which is also mentioned in the premise
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the travel distance in the premise contradicts the estimate of less than 'travel_distance_hypothesis'
    label = "contradiction"
else:
    # if the travel distance in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
