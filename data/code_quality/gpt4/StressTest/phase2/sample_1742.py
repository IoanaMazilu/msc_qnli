investment_rate_premise = 12
investment_rate_hypothesis = 72

# the hypothesis talks about the investment rate, referenced also in the premise
if investment_rate_hypothesis == investment_rate_premise:
    # check if the investment rates are the same
    label = "entailment"
elif investment_rate_hypothesis != investment_rate_premise:
    # check if the investment rate in the hypothesis contradicts the investment rate reported in the premise
    label = "contradiction"

print(label)
