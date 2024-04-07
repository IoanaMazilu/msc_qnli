# Premise: 1620 in 8% stock, Michael earns Rs.
# Hypothesis: less than 1620 in 8% stock, Michael earns Rs.
# Golden Label: contradiction

stock_value_premise = 1620
stock_value_hypothesis = 1620

# the hypothesis talks about the amount of money in stock, also mentioned in the premise
if stock_value_hypothesis < stock_value_premise:
    # check if the hypothesis value contradicts the explicit amount of 'stock_value_premise'
    label = "contradiction"
elif stock_value_hypothesis == stock_value_premise:
    # if the hypothesis value and premise value are exactly the same, we can infer entailment
    label = "entailment"
else:
    # any value of 'stock_value_hypothesis' greater than 'stock_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

