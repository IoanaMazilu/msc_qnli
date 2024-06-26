water_storage_premise = 48
water_storage_hypothesis = 28

# the hypothesis refers to the amount of water stored in gallon jars mentioned in the premise
if water_storage_hypothesis >= water_storage_premise:
    # check if the 'water_storage_hypothesis' contradicts the premise of less than 'water_storage_premise' gallons
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of water
    # any amount of water less than 'water_storage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
