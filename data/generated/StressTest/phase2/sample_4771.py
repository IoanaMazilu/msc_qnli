# Premise: If Mary received $more than 500 more than Harry did, what was the profit made by their business in that year?
# Hypothesis: If Mary received $800 more than Harry did, what was the profit made by their business in that year?
# Golden Label: neutral

mary_profit_premise = 500
mary_profit_hypothesis = 800

# the hypothesis refers to the profit made by Mary compared to Harry
if mary_profit_hypothesis <= mary_profit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'mary_profit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit made by Mary
    # any profit made by Mary greater than 'mary_profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

