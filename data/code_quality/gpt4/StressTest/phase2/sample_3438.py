water_gallons_premise = 28
water_gallons_hypothesis = 48

# the hypothesis refers to the amount of water stored which is also mentioned in the premise
if water_gallons_premise > water_gallons_hypothesis:
    # check if the amount of water in premise contradicts the estimate of 'water_gallons_hypothesis'
    label = "contradiction"
else:
    # if the amount of water in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
