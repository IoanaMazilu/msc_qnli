investment_premise = 20000
investment_hypothesis = 20000
months_premise = 7
months_hypothesis = 6

# the hypothesis refers to the amount invested and the duration of investment mentioned in the premise
if investment_premise!= investment_hypothesis:
    # check if the amount invested in the hypothesis contradicts the amount invested in the premise
    label = "contradiction"
elif months_hypothesis >= months_premise:
    # check if the duration of investment in the hypothesis contradicts the duration of investment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of investment
    # any duration of investment less than'months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
