# Premise: On the first day of her vacation, Louisa traveled 100 miles.
# Hypothesis: On the first day of her vacation, Louisa traveled less than 300 miles.
# Golden Label: entailment

travel_distance_premise = 100
travel_distance_hypothesis = 300

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the premise value contradicts the estimate of less than 'travel_distance_hypothesis'
    label = "contradiction"
elif travel_distance_premise != travel_distance_hypothesis:
    # the premise provides a specific number for the distance traveled
    # any distance less than 'travel_distance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

