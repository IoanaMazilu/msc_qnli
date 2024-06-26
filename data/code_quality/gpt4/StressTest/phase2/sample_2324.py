water_added_premise = 6
water_added_hypothesis = 6
tank_fill_premise = 7/8
tank_fill_hypothesis = 7/8

# the hypothesis refers to the amount of water Henry adds to the tank and the resulting tank fill level
if water_added_hypothesis >= water_added_premise:
    # check if the hypothesis value contradicts the premise stating that Henry adds exactly 'water_added_premise' gallons
    label = "contradiction"
elif tank_fill_hypothesis != tank_fill_premise:
    # check if the resulting tank fill level in the hypothesis contradicts the level reported in the premise
    label = "contradiction"
else:
    # if no contradiction is found, we can infer entailment
    label = "entailment"

print(label)
