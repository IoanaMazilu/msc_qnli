withdraw_premise = 2000
withdraw_hypothesis = 5000

# the hypothesis talks about the amount Tony withdraws, referenced also in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact amount
    # any amount greater than 'withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
