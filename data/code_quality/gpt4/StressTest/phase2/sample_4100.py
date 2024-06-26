investment_premise = 1000000
investment_hypothesis = 1000000

# The hypothesis refers to the amount of money invested by Raviraj, which is also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, then it's consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
