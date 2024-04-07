# Premise: Jill has 35 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has 85 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: contradiction

water_storage_premise = 35
water_storage_hypothesis = 85

# The premise and hypothesis refer to the same amount of water stored by Jill
if water_storage_hypothesis != water_storage_premise:
    # Check if the amount of water in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # If the amount of water in the hypothesis is equal to the amount in the premise, we can infer entailment
    label = "entailment"

print(label)

