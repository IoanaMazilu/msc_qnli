# Premise: 1620 in 8% stock, Michael earns Rs.
# Hypothesis: less than 4620 in 8% stock, Michael earns Rs.
# Golden Label: entailment

stock_value_premise = 1620
stock_value_hypothesis = 4620

# the hypothesis talks about the value of the stock that Michael owns, referenced also in the premise
if stock_value_hypothesis <= stock_value_premise:
    # check if the value of stock in the hypothesis contradicts the value of stock in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the stock
    # any stock value greater than 'stock_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

