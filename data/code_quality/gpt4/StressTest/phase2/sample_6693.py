withdraw_premise = 14000
withdraw_hypothesis = 44000

# the hypothesis refers to the amount withdrawn by John, also mentioned in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the hypothesis value contradicts the premise value of 'withdraw_premise'
    label = "contradiction"
elif withdraw_premise >= withdraw_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'withdraw_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific amount withdrawn by John
    # any amount less than 'withdraw_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
