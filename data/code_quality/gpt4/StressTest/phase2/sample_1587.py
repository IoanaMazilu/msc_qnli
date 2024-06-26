withdraw_premise = 4000
withdraw_hypothesis = 2000

# the hypothesis talks about the amount Bhavan withdraws, referenced also in the premise
if withdraw_hypothesis >= withdraw_premise:
    # check if the hypothesis value contradicts the statement of 'withdraw_premise' more
    label = "contradiction"
else:
    # premise clearly states that the withdrawal amount is 'withdraw_premise' more
    # any value less than 'withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
