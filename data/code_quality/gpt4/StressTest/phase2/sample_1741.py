investment_rate_premise = 82
investment_rate_hypothesis = 12

# the hypothesis refers to the investment rate mentioned in the premise
if investment_rate_hypothesis >= investment_rate_premise:
    # check if the 'investment_rate_hypothesis' contradicts the premise of less than 'investment_rate_premise'
    label = "contradiction"
else:
    # if the 'investment_rate_hypothesis' is less than 'investment_rate_premise', we can infer entailment
    label = "entailment"

print(label)
