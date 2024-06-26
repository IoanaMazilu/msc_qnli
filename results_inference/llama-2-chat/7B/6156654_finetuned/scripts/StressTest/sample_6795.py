deposit_premise = 62500
deposit_hypothesis = 22500

# the hypothesis refers to the amount Lucy deposited in the investment fund, which is also mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    label = "neutral"

print(label)
