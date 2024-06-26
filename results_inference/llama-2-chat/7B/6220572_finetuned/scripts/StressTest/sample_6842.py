investment_time_premise = 6
investment_time_hypothesis = 6

# the hypothesis refers to the investment time mentioned in the premise
if investment_time_hypothesis <= investment_time_premise:
    # check if the hypothesis value contradicts the investment time in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment time
    # any investment time greater than 'investment_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
