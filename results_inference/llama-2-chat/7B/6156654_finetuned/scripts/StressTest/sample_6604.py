investment_return_premise = 3
investment_return_hypothesis = 2

# the hypothesis talks about the investment return, which is also mentioned in the premise
if investment_return_hypothesis <= investment_return_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif investment_return_hypothesis > investment_return_premise:
    # if the hypothesis value is greater than the premise value, it does not contradict it
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it does not contradict it
    label = "neutral"

print(label)
