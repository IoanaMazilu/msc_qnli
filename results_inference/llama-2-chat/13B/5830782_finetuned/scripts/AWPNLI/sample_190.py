crayons_initial_premise = 479.0
crayons_remaining_premise = 134.0
crayons_lost_hypothesis = 345.0

# the hypothesis refers to the number of crayons that were lost or given away, which can be inferred from the premise
# compute the number of crayons that were lost or given away in the premise
crayons_lost_premise = crayons_initial_premise - crayons_remaining_premise
if crayons_lost_hypothesis!= crayons_lost_premise:
    # check if the number of crayons lost in the hypothesis contradicts the number of crayons lost from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
