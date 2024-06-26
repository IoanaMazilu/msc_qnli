investment_premise = 20000
investment_hypothesis = 20000
investment_time_premise = 6
investment_time_hypothesis = 6

# the hypothesis refers to the amount and time of investment mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount of investment in the hypothesis contradicts the amount of investment reported in the premise
    label = "contradiction"
elif investment_time_hypothesis <= investment_time_premise:
    # check if the time of investment in the hypothesis contradicts the time of investment reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of investment
    # any time of investment greater than 'investment_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
