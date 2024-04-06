# Premise: Saudi Prince, billionaire says'never' again to $100 oil barrel.
# Hypothesis: Saudi Prince Says Oil Will'Never Reach $100 Per Barrel Again'
# Golden Label: entailment

oil_price_premise = 100
oil_price_hypothesis = 100

# the hypothesis and premise mention the same oil price level that will never be reached again according to the Saudi Prince
if oil_price_hypothesis != oil_price_premise:
    # check if the oil price in the hypothesis contradicts the oil price in the premise
    label = "contradiction"
else:
    # if the oil price in the hypothesis does not contradict the oil price in the premise, we can infer entailment
    label = "entailment"

print(label)

