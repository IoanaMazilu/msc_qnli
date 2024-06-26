investment_premise = 1000000000
investment_hypothesis = 1000000000

# the premise mentions a specific amount of investment, while the hypothesis mentions the same amount
if investment_hypothesis == investment_premise:
    label = "entailment"
else:
    # check if the amount of investment in the hypothesis contradicts the premise amount
    label = "contradiction"

print(label)
