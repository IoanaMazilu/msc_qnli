price_premise = 20
price_hypothesis = 20

# the hypothesis and premise mention the potential price of oil
if price_premise != price_hypothesis:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis price does not contradict the premise price, we can infer entailment
    label = "entailment"

print(label)
