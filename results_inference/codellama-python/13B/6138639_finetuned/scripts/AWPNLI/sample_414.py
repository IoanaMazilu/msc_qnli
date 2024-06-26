total_crayons_premise = 7.0 + 3.0
total_crayons_hypothesis = 10.0

# the hypothesis refers to the total number of crayons, which are also mentioned in the premise
# check if the total number of crayons in the hypothesis contradicts the total number of crayons from the premise
if total_crayons_hypothesis!= total_crayons_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
