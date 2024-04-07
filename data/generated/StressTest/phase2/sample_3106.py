# Premise: Jill has less than 52 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has 42 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: neutral

water_storage_premise = 52
water_storage_hypothesis = 42

# The hypothesis refers to the amount of water stored mentioned in the premise
if water_storage_hypothesis >= water_storage_premise:
    # Check if the value in the hypothesis contradicts the premise of less than 'water_storage_premise'
    label = "contradiction"
elif water_storage_hypothesis < water_storage_premise:
    # Any amount of water less than 'water_storage_premise' is consistent with the premise and can be explicitly entailed
    label = "entailment"

print(label)

