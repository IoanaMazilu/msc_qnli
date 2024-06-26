ratio_premise = 144/25
ratio_hypothesis = 544/25
bc_premise = 13
bc_hypothesis = 13

# the hypothesis refers to the ratio of areas and the length of BC mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif bc_hypothesis!= bc_premise:
    # check if the length of BC in the hypothesis contradicts the length of BC in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
