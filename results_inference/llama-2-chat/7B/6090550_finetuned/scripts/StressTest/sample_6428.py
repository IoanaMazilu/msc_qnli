sold_price_premise = 450
sold_price_hypothesis = 750

# the hypothesis refers to the price of something that was sold, which is also mentioned in the premise
if sold_price_hypothesis!= sold_price_premise:
    # check if the sold price in the hypothesis contradicts the sold price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
