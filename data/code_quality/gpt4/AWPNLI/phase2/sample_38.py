crayons_drawer_premise = 7.0
crayons_taken_premise = 3.0
crayons_drawer_hypothesis = 4.0

# the hypothesis refers to the number of crayons in the drawer, which is also mentioned in the premise
# compute the number of crayons left in the drawer in the premise
crayons_left_premise = crayons_drawer_premise - crayons_taken_premise
if crayons_drawer_hypothesis != crayons_left_premise:
    # check if the number of crayons in the drawer in the hypothesis contradicts the number of crayons left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
