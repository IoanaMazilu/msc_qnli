pens_purchased_premise = 12
pens_purchased_hypothesis = 12

# the hypothesis refers to the number of pens purchased mentioned in the premise
if pens_purchased_hypothesis >= pens_purchased_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
