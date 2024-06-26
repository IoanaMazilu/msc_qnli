reena_investment_premise = 35000
reena_investment_duration_premise = 8
reena_investment_duration_hypothesis = 1

# the hypothesis talks about the investment of Reena and Shaloo in a business, referenced also in the premise
if reena_investment_duration_hypothesis > reena_investment_duration_premise:
    # check if the investment duration of Reena in the hypothesis contradicts the investment duration mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact investment of Reena and duration of investment
    # but the duration of investment in the hypothesis is less than the premise. Hence, it does not contradict, but it cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
