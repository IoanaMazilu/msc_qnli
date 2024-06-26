withdrawal_amount_premise = 2000
withdrawal_amount_hypothesis = 5000

# the hypothesis talks about the amount of withdrawal, referenced also in the premise
if withdrawal_amount_hypothesis <= withdrawal_amount_premise:
    # check if the hypothesis value contradicts the amount of withdrawal in the premise
    label = "contradiction"
else:
    # any amount greater than 'withdrawal_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
