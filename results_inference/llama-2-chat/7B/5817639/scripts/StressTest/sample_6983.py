rate_premise = 6
rate_hypothesis = 8

# the hypothesis talks about a different interest rate than the premise
if rate_hypothesis >= rate_premise:
    # check if the hypothesis rate contradicts the premise rate
    label = "contradiction"
else:
    # the hypothesis rate is consistent with the premise rate, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
