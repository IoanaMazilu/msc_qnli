price_premise = 90
price_hypothesis = 90

# the hypothesis talks about the price of the item in Store Z, which is also mentioned in the premise
if price_hypothesis < price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis price does not contradict the premise price, we can infer entailment
    label = "entailment"

print(label)
