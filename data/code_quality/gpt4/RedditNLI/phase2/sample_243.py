gold_price_premise = 1500
gold_price_hypothesis = 1500

# the hypothesis and premise mention the price of gold reaching a historic level
if gold_price_hypothesis != gold_price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis price does not contradict the premise price, we can infer entailment
    label = "entailment"

print(label)
