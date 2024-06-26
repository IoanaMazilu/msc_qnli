crayons_in_drawer_premise = 7.0
crayons_taken_premise = 3.0
crayons_left_hypothesis = 0.0

# the hypothesis refers to the number of crayons left, which can be computed from the premise
# compute the number of crayons left in the premise
crayons_left_premise = crayons_in_drawer_premise - crayons_taken_premise
if crayons_left_hypothesis!= crayons_left_premise:
    # check if the number of crayons left in the hypothesis contradicts the number of crayons left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)