crayons_drawer_premise = 7.0
crayons_added_premise = 3.0
crayons_drawer_hypothesis = 10.0

# the hypothesis refers to the number of crayons in the drawer, which is also mentioned in the premise
# compute the total number of crayons in the drawer from the premise
total_crayons_drawer_premise = crayons_drawer_premise + crayons_added_premise
if crayons_drawer_hypothesis!= total_crayons_drawer_premise:
    # check if the number of crayons in the drawer from the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
