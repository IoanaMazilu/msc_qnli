sitting_owls_premise = 3.0
joined_owls_premise = 2.0
sitting_owls_hypothesis = 3.0

# the hypothesis refers to the number of owls, which are also mentioned in the premise
# compute the total number of owls in the premise
total_owls_premise = sitting_owls_premise + joined_owls_premise
if sitting_owls_hypothesis != total_owls_premise:
    # check if the number of owls in the hypothesis contradicts the number of owls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
