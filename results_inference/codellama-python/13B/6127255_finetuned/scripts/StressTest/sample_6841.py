investment_premise = 20000
investment_hypothesis = 20000
investment_time_premise = 7
investment_time_hypothesis = 6

# the hypothesis refers to the amount invested and the time period mentioned in the premise
if investment_premise!= investment_hypothesis:
    # check if the amount invested in the hypothesis contradicts the amount invested in the premise
    label = "contradiction"
elif investment_time_hypothesis >= investment_time_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the time period
    # any time period less than 'investment_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
