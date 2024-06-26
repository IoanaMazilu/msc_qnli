debt_increase_premise = 57
debt_increase_hypothesis = 57
years_post_crisis_hypothesis = 7

# the hypothesis and premise mention the increase in global debt since the 2007-08 financial crisis
if debt_increase_premise!= debt_increase_hypothesis:
    # check if the debt increase in the hypothesis contradicts the debt increase in the premise
    label = "contradiction"
else:
    # the premise does not provide information about the time period after the crisis
    # the hypothesis' time period is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
