sold_premise = 450
sold_hypothesis = 750

# the hypothesis refers to the amount of money that was sold, mentioned in the premise
if sold_premise >= sold_hypothesis:
    # check if the estimate of'sold_hypothesis' contradicts the amount of money sold in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
