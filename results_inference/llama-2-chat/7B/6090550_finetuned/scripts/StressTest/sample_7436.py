store_z_premise = 90
store_z_hypothesis = 90

# the hypothesis refers to the value of'store_z_premise'
if store_z_hypothesis!= store_z_premise:
    # check if the value of'store_z_hypothesis' contradicts the value of'store_z_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
