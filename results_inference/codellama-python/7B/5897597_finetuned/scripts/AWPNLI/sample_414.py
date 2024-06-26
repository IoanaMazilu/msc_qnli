crayons_drawer_premise = 7.0
added_crayons_premise = 3.0
total_crayons_hypothesis = 10.0

# the hypothesis refers to the total number of crayons, which are also mentioned in the premise
# compute the total number of crayons in the premise
total_crayons_premise = crayons_drawer_premise + added_crayons_premise
if total_crayons_hypothesis!= total_crayons_premise:
    # check if the total number of crayons in the hypothesis contradicts the total number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
