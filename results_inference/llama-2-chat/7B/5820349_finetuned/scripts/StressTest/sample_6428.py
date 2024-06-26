sold_price_premise = 450
sold_price_hypothesis = 750

# the hypothesis refers to the price at which something was sold, which is also mentioned in the premise
if sold_price_hypothesis!= sold_price_premise:
    # check if the price in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
