investment_premise = 20000
investment_hypothesis = 20000
months_premise = 7
months_hypothesis = 6

# the hypothesis refers to the amount invested and the period of investment mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
elif months_hypothesis >= months_premise:
    # check if the period of investment in the hypothesis contradicts the period of investment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the period of investment
    # any period of investment less than'months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
