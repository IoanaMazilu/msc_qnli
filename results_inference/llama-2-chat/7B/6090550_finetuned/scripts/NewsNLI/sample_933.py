# the hypothesis is about the length of the slab
# the premise mentions the weight of the slab and its composition
# we can calculate the total weight of the slab based on the premise
# but we cannot infer the length of the slab from the premise
total_weight = 40000 + (85/100) * weight_composition
total_weight_premise = 40000
if total_weight_premise!= total_weight:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # if the total weight in the hypothesis does not contradict the total weight in the premise
    # we can infer entailment
    label = "entailment"

print(label)
