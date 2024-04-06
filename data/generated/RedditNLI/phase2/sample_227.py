# Premise: Amazon buying Whole Foods for $13.7B.
# Hypothesis: Amazon to buy Whole Foods for $13.7bn.
# Golden Label: entailment

price_premise = 13.7
price_hypothesis = 13.7

# the hypothesis and premise mention the price for which Amazon is buying Whole Foods
if price_hypothesis != price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis price does not contradict the premise price, we can infer entailment
    label = "entailment"

print(label)

