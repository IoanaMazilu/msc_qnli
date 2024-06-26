initial_crayons_premise = 479.0
remaining_crayons_premise = 134.0
lost_crayons_hypothesis = 345.0

# the hypothesis refers to the number of lost crayons, which can be inferred from the premise
# compute the number of lost crayons in the premise
lost_crayons_premise = initial_crayons_premise - remaining_crayons_premise
if lost_crayons_hypothesis!= lost_crayons_premise:
    # check if the number of lost crayons in the hypothesis contradicts the number of lost crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
