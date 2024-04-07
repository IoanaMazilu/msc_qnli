# Premise: Jill has 7 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has more than 4 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: entailment

water_stored_premise = 7
water_stored_hypothesis = 4

# the hypothesis refers to the volume of stored water mentioned in the premise
if water_stored_premise <= water_stored_hypothesis:
    # check if the estimate of 'water_stored_hypothesis' contradicts the volume of stored water in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

