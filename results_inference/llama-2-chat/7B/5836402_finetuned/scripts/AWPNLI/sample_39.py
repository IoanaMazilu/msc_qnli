crayons_initial_premise = 7.0
taken_crayons_premise = 3.0
crayons_hypothesis = 0.0

# the hypothesis refers to the number of crayons, which are also mentioned in the premise
# compute the number of crayons left in the premise
crayons_left_premise = crayons_initial_premise - taken_crayons_premise
if crayons_hypothesis!= crayons_left_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
