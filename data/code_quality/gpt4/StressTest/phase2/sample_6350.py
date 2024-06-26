investment_premise = 90000
investment_hypothesis = 90000

# The hypothesis refers to the amount of investment made by Mr Praveen mentioned in the premise
if investment_hypothesis != investment_premise:
    # Check if the amount of investment in the hypothesis contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # Since the hypothesis states that the investment is more than the amount mentioned, and the premise confirms that the investment is exactly that amount
    # It is a neutral case, not a direct entailment or contradiction
    label = "neutral"

print(label)
