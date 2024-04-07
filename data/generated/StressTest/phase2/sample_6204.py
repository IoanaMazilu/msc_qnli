# Premise: 20 each, are purchased from Ram by Mohan at a price of Rs.
# Hypothesis: less than 60 each, are purchased from Ram by Mohan at a price of Rs.
# Golden Label: entailment

purchase_price_premise = 20
purchase_price_hypothesis = 60

# the hypothesis speaks about the purchase price mentioned in the premise
if purchase_price_hypothesis <= purchase_price_premise:
    # check if the hypothesis price contradicts the premise price
    label = "contradiction"
else:
    # any price less than 'purchase_price_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

