profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis talks about the profit in the business at the end of the year
# the premise mentions the amount Mr Praveen would have received as the profit
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the amount Mr Praveen would have received as the profit
    # any amount greater than the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
