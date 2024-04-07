# Premise: On the first day of her vacation, Louisa traveled 250 miles.
# Hypothesis: On the first day of her vacation, Louisa traveled less than 350 miles.
# Golden Label: entailment

travel_distance_premise = 250
travel_distance_hypothesis = 350

# the hypothesis refers to the distance Louisa traveled on the first day of her vacation
if travel_distance_premise >= travel_distance_hypothesis:
    # check if the distance traveled in the premise contradicts the claim in the hypothesis of being less than 'travel_distance_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact distance traveled
    # any distance less than 'travel_distance_hypothesis' and greater or equal to 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

