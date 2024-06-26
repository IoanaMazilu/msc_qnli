water_gallons_premise = 55
water_gallons_hypothesis = 35

# the hypothesis refers to the amount of stored water in gallons mentioned in the premise
if water_gallons_hypothesis >= water_gallons_premise:
    # check if the 'water_gallons_hypothesis' contradicts the estimate of less than 'water_gallons_premise'
    label = "contradiction"
elif water_gallons_hypothesis < water_gallons_premise:
    # check if the 'water_gallons_hypothesis' can be fully entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and cannot be entailed, we infer neutral
    label = "neutral"

print(label)
