total_pens_purchased_premise = 12
total_pens_purchased_hypothesis = 52

# the hypothesis refers to the total number of pens Elena purchased, which is also mentioned in the premise
if total_pens_purchased_hypothesis != total_pens_purchased_premise:
    # check if the total number of pens purchased in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)