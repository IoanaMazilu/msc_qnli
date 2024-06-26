deposit_premise = 62500
deposit_hypothesis = 52500

# the hypothesis refers to the amount deposited in the investment fund mentioned in the premise
if deposit_hypothesis!= deposit_premise:
    # check if the hypothesis value contradicts the amount deposited in the premise
    label = "contradiction"
else:
    # the premise gives the amount deposited and the hypothesis does not contradict it
    # any amount deposited in the investment fund is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
