ratio_premise = 144/25
ratio_hypothesis = 244/25
bc_premise = 13
bc_hypothesis = 13

# the hypothesis refers to the ratio of areas and BC mentioned in the premise
if ratio_premise!= ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif bc_premise!= bc_hypothesis:
    # check if the BC in the hypothesis contradicts the BC in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
