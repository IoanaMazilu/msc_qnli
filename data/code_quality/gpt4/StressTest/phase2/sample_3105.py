water_gallons_premise = 42
water_gallons_hypothesis = 52

# the hypothesis refers to the amount of stored water mentioned in the premise
if water_gallons_hypothesis <= water_gallons_premise:
    # check if the 'water_gallons_hypothesis' contradicts the amount of water in the premise
    label = "contradiction"
elif water_gallons_hypothesis != water_gallons_premise:
    # check if the amount of water in the hypothesis contradicts the amount of water reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
