# Premise: less than 7620 in 8% stock, Michael earns Rs.
# Hypothesis: 1620 in 8% stock, Michael earns Rs.
# Golden Label: neutral

stock_value_premise = 7620
stock_value_hypothesis = 1620

# the hypothesis refers to the same stock value as the premise
if stock_value_hypothesis >= stock_value_premise:
    # check if the hypothesis value contradicts the premise of less than 'stock_value_premise'
    label = "contradiction"
elif stock_value_hypothesis < stock_value_premise:
    # the premise gives only an estimate for the stock value
    # any stock value less than 'stock_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

