purchase_price_premise = 15000
purchase_price_hypothesis = 25000
profit_premise = 0.20
profit_hypothesis = 0.20

# the hypothesis talks about the purchase price and the expected profit, both also mentioned in the premise
if purchase_price_premise != purchase_price_hypothesis:
    # check if the purchase price in the hypothesis contradicts the purchase price in the premise
    label = "contradiction"
elif profit_premise != profit_hypothesis:
    # check if the expected profit in the hypothesis contradicts the expected profit in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
