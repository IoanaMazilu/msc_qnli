# Premise: There are 7.0 crayons in the drawer and Mary put 3.0 more crayons in the drawer.
# Hypothesis: 9.0 crayons are in the drawer now.
# Golden Label: contradiction

crayons_drawer_premise = 7.0
crayons_added_premise = 3.0
total_crayons_hypothesis = 9.0

# the hypothesis refers to the total number of crayons, which are also mentioned in the premise
# calculate the total number of crayons in the premise
total_crayons_premise = crayons_drawer_premise + crayons_added_premise
if total_crayons_hypothesis != total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

