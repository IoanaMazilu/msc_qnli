crayons_drawer_premise = 7.0
crayons_taken_premise = 3.0
crayons_hypothesis = 0.0

# the hypothesis refers to the number of crayons, which is also mentioned in the premise
# compute the remaining number of crayons in the premise
remaining_crayons_premise = crayons_drawer_premise - crayons_taken_premise
if crayons_hypothesis != remaining_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of remaining crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
