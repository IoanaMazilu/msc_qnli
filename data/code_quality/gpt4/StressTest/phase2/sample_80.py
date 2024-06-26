water_added_premise = 9
water_added_hypothesis = 9
tank_capacity_premise_fullness_before = 3/4
tank_capacity_premise_fullness_after = 7/8

# the hypothesis talks about the amount of water added to a tank and its fullness, referenced also in the premise
if water_added_hypothesis <= water_added_premise:
    # check if the hypothesis value contradicts the estimate of more than 'water_added_premise'
    label = "contradiction"
else:
    # the premise gives a specific amount of water to be added to reach a certain level of fullness
    # any amount of water greater than 'water_added_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
