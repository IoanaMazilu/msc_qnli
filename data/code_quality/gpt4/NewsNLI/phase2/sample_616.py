cost_premise = 1.5e9
sale_price_hypothesis = 150e6

# the hypothesis mentions the cost of the airport and the sale price, which are also referenced in the premise
if sale_price_hypothesis > cost_premise:
    # check if the sale price in the hypothesis contradicts the cost reported in the premise
    label = "contradiction"
else:
    # if the sale price does not contradict the cost, we can infer entailment
    label = "entailment"

print(label)