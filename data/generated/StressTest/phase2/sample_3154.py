# Premise: If Henry were to add more than 5 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add 7 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: neutral

water_added_premise = 5
water_added_hypothesis = 7

# the hypothesis talks about the amount of water added to a tank, referenced also in the premise
if water_added_hypothesis <= water_added_premise:
    # check if the amount of water added in the hypothesis contradicts the premise's estimate of more than 'water_added_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of water to be added
    # any amount of water greater than 'water_added_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

