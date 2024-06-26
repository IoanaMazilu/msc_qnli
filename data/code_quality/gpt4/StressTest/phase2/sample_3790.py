water_gallons_premise = 51
water_gallons_hypothesis = 21

# the hypothesis refers to the amount of water Jill has stored, mentioned in the premise
if water_gallons_hypothesis >= water_gallons_premise:
    # check if the amount of water in the hypothesis contradicts the premise of having less than 'water_gallons_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of water
    # any amount of water less than 'water_gallons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
