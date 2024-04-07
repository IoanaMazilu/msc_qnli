# Premise: 1620 in 8% stock, Michael earns Rs.
# Hypothesis: more than 1620 in 8% stock, Michael earns Rs.
# Golden Label: contradiction

stock_investment_premise = 1620
stock_investment_hypothesis = 1620

# the hypothesis refers to the stock investment mentioned in the premise
if stock_investment_hypothesis <= stock_investment_premise:
    # check if the estimate of 'stock_investment_hypothesis' contradicts the stock investment in the premise
    label = "contradiction"
else:
    # the premise gives the exact value for the stock investment
    # any value greater than 'stock_investment_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

