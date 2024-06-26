crayons_drawer_premise = 7.0
put_crayons_premise = 3.0
total_crayons_hypothesis = 10.0

# the hypothesis refers to the number of crayons in the drawer, which are also mentioned in the premise
# compute the total number of crayons in the premise
total_crayons_premise = crayons_drawer_premise + put_crayons_premise
if total_crayons_hypothesis!= total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
