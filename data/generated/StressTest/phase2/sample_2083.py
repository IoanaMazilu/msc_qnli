# Premise: If Henry were to add more than 3 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add 4 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: neutral

water_added_premise = 3
water_added_hypothesis = 4

# the hypothesis refers to the amount of water Henry adds to the tank, which is also mentioned in the premise
if water_added_hypothesis <= water_added_premise:
    # check if the hypothesis value contradicts the estimate of more than 'water_added_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of water added
    # any amount of water greater than 'water_added_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

