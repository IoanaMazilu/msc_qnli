water_added_premise = 8
water_added_hypothesis = 2
tank_fill_premise = 7/8
tank_fill_hypothesis = 7/8

# the hypothesis is about the quantity of water added to a tank and the resulting fill level, which is the same context as the premise
if water_added_hypothesis != water_added_premise:
    # check if the quantity of water added in the hypothesis contradicts the quantity of water added in the premise
    label = "contradiction"
elif tank_fill_hypothesis != tank_fill_premise:
    # check if the fill level of the tank in the hypothesis contradicts the fill level of the tank in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the ones in the premise, but they do not match either, we can infer neutrality
    label = "neutral"

print(label)
