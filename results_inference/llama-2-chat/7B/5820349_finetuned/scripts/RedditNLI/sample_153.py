rate_premise = 1
rate_hypothesis = 25

# the hypothesis and premise mention different rates for U.S.
if rate_hypothesis > rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise and hypothesis do not contradict each other, but the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
