purchased_price_premise = 20
purchased_price_hypothesis = 20

# the hypothesis refers to the price of purchased items mentioned in the premise
if purchased_price_hypothesis <= purchased_price_premise:
    # check if the estimate of 'purchased_price_hypothesis' contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
