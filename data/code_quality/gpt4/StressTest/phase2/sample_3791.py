water_storage_premise = 21
water_storage_hypothesis = 31

# the hypothesis refers to the amount of water stored by Jill, also mentioned in the premise
if water_storage_premise != water_storage_hypothesis:
    # check if the quantity of water stored in the hypothesis contradicts the quantity stated in the premise
    label = "contradiction"
else:
    label = "entailment"

print(label)
