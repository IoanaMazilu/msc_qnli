pens_purchased_premise = 12
pens_purchased_hypothesis = 12

# the hypothesis refers to the number of pens purchased by Elena mentioned in the premise
if pens_purchased_hypothesis <= pens_purchased_premise:
    # check if the hypothesis value contradicts the number of pens purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
