# Premise: The first act included 5.0 clown mobiles, each stuffed with 28.0 clowns.
# Hypothesis: 143.0 clowns are inside all the clown mobiles combined.
# Golden Label: contradiction

clown_mobiles_premise = 5.0
clowns_per_mobile_premise = 28.0
total_clowns_hypothesis = 143.0

# the hypothesis refers to the total number of clowns, which is also mentioned in the premise
# compute the total number of clowns in the premise
total_clowns_premise = clown_mobiles_premise * clowns_per_mobile_premise
if total_clowns_hypothesis != total_clowns_premise:
    # check if the number of clowns in the hypothesis contradicts the number of clowns from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

