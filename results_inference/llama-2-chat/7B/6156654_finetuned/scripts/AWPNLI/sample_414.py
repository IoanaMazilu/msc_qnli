crayons_premise = 7.0
crayons_added_premise = 3.0
total_crayons_hypothesis = 10.0

# the hypothesis refers to the total number of crayons, which is also mentioned in the premise
# compute the total number of crayons in the premise
total_crayons_premise = crayons_premise + crayons_added_premise
if total_crayons_hypothesis!= total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values are the same, we can infer entailment
    label = "entailment"

print(label)
