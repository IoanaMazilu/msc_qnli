water_storage_premise = 14
water_storage_hypothesis = 54

# the hypothesis refers to the amount of water stored mentioned in the premise
if water_storage_premise >= water_storage_hypothesis:
    # check if the amount of water in the premise contradicts the estimate of less than 'water_storage_hypothesis'
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
