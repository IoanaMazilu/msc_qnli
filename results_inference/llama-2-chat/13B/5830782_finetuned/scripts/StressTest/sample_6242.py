ratio_premise = 144/25
ratio_hypothesis = 244/25
bc_premise = 13
bc_hypothesis = 13

# the hypothesis refers to the ratio of areas and BC mentioned in the premise
if ratio_premise!= ratio_hypothesis:
    # check if the ratio of areas in the hypothesis contradicts the ratio of areas in the premise
    label = "contradiction"
elif bc_hypothesis!= bc_premise:
    # check if the value of BC in the hypothesis contradicts the value of BC in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
