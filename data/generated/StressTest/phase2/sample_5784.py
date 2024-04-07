# Premise: Vijay sells a cupboard at 10% below cost price.
# Hypothesis: Vijay sells a cupboard at less than 60% below cost price.
# Golden Label: entailment

selling_price_premise = 10
selling_price_hypothesis = 60

# the hypothesis talks about the selling price of the cupboard, referenced also in the premise
if selling_price_hypothesis < selling_price_premise:
    # check if the hypothesis value contradicts the estimate of 'selling_price_premise' percent below the cost price
    label = "contradiction"
elif selling_price_hypothesis == selling_price_premise:
    # check if the selling price in the hypothesis matches the selling price reported in the premise
    label = "entailment"
else:
    # the premise gives a specific selling price below the cost price
    # any selling price greater than 'selling_price_premise' and less than the cost price is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

