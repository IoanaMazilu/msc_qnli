# Premise: Jill has 42 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has less than 42 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: contradiction

water_storage_premise = 42
water_storage_hypothesis = 42

# the hypothesis refers to the exact amount of water storage mentioned in the premise
if water_storage_hypothesis >= water_storage_premise:
    # check if the amount of 'water_storage_hypothesis' contradicts the number of water storage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

