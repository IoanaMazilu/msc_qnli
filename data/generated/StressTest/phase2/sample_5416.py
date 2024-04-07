# Premise: If Lary received $more than 200 more than Terry did, what was the profit made by their business in that year?
# Hypothesis: If Lary received $800 more than Terry did, what was the profit made by their business in that year?
# Golden Label: neutral

lary_profit_premise = 200
lary_profit_hypothesis = 800

# the hypothesis refers to the profit Lary made, which is also mentioned in the premise
if lary_profit_hypothesis <= lary_profit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lary_profit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit Lary made
    # any profit made by Lary greater than 'lary_profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

