# Premise: Jill has less than 54 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has 14 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: neutral

water_storage_premise = 54
water_storage_hypothesis = 14

# the hypothesis talks about the quantity of water storage, which is also referenced in the premise
if water_storage_hypothesis >= water_storage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'water_storage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of water storage
    # any amount of water less than 'water_storage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

