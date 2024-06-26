withdraw_premise = 5000
withdraw_hypothesis = 2000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdraw_hypothesis >= withdraw_premise:
    # check if the hypothesis value contradicts the estimate of less than 'withdraw_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount Tony withdraws
    # any amount less than 'withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
