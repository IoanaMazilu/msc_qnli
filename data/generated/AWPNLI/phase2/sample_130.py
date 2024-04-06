# Premise: 3.0 owls were sitting on the fence and 2.0 more owls joined them.
# Hypothesis: 5.0 owls are on the fence now.
# Golden Label: entailment

sitting_owls_premise = 3.0
joined_owls_premise = 2.0
total_owls_hypothesis = 5.0

# the hypothesis refers to the total number of owls on the fence, which is also mentioned in the premise
# compute the total number of owls in the premise
total_owls_premise = sitting_owls_premise + joined_owls_premise
if total_owls_hypothesis != total_owls_premise:
    # check if the total number of owls in the hypothesis contradicts the total number of owls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

