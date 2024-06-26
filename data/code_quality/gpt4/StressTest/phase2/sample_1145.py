pets_total_premise = 92
pets_total_hypothesis = 12

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if pets_total_hypothesis != pets_total_premise:
    # check if the total number of pets in the hypothesis contradicts the total number of pets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
