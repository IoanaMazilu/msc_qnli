# Premise: Jill has 28 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has 38 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: contradiction

water_storage_premise = 28
water_storage_hypothesis = 38

# the hypothesis refers to the same amount of water storage mentioned in the premise
if water_storage_hypothesis != water_storage_premise:
    # check if the water storage amount in the hypothesis contradicts the water storage amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

