# Premise: Citi: Oil Could Plunge to $20, and This Might Be'the End of OPEC'
# Hypothesis: Oil Plunge To $20 Could Be On The Horizon, Citigroup Warns.
# Golden Label: entailment

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

