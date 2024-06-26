#ratio_premise = 144/25
#ratio_hypothesis = 544/25
#bc_premise = 13
#bc_hypothesis = 13

# the hypothesis refers to the ratio of areas and BC mentioned in the premise
# if the ratio of areas or BC in the hypothesis contradicts the ratio of areas or BC in the premise, we can infer contradiction
if ratio_hypothesis < ratio_premise or bc_hypothesis!= bc_premise:
    label = "contradiction"
# if the ratio of areas and BC in the hypothesis do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
#