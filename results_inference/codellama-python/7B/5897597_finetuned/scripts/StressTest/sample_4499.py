discount_premise = 12
discount_hypothesis = 12

# the hypothesis refers to the discount percentage on the cupboard's cost price mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
