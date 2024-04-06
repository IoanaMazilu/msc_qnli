# Premise: Ethereum Jumps To $400! June 12 2017 Medium.
# Hypothesis: Ethereum Hit $300 June 10th 2017 Medium.
# Golden Label: neutral

ethereum_price_premise = 400
ethereum_price_hypothesis = 300

# the hypothesis and premise mention the price of Ethereum at some point in time
if ethereum_price_hypothesis > ethereum_price_premise:
    # check if the price of Ethereum in the hypothesis contradicts the price of Ethereum in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

