# Premise: On the first day of her vacation, Louisa traveled 200 miles.
# Hypothesis: On the first day of her vacation, Louisa traveled less than 300 miles.
# Golden Label: entailment

travel_distance_premise = 200
travel_distance_hypothesis = 300

# the hypothesis refers to the distance traveled by Louisa on her first vacation day, which is also mentioned in the premise
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the traveled distance in the premise contradicts the estimate of 'travel_distance_hypothesis'
    label = "contradiction"
else:
    # if the distance in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

