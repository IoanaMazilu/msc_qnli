purchase_price_premise = 1000000000
purchase_price_hypothesis = 1000000000

# the hypothesis mentions the purchase price of Instagram by Facebook, which is also mentioned in the premise
if purchase_price_hypothesis!= purchase_price_premise:
    # check if the purchase price in the hypothesis contradicts the purchase price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
