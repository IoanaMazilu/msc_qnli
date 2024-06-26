investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the amount invested by Mr Praveen, mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact amount invested
    # any amount greater than 'investment_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
