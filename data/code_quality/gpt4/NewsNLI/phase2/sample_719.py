purchase_price_premise = 1000000000
purchase_price_hypothesis = 1000000000

# the hypothesis mentions the purchase price of Instagram by Facebook, which is also mentioned in the premise
if purchase_price_hypothesis != purchase_price_premise:
    # check if the purchase price in the hypothesis contradicts the purchase price reported in the premise
    label = "contradiction"
else:
    # if the purchase price in the hypothesis does not contradict the premise, it remains neutral or entailment
    # the hypothesis also mentions a need for return, which cannot be entailed from the premise
    label = "neutral"

print(label)
