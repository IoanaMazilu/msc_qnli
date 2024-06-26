withdrawal_premise = 2000
withdrawal_hypothesis = 5000

# the hypothesis refers to the amount of withdrawal mentioned in the premise
if withdrawal_hypothesis >= withdrawal_premise:
    # check if the hypothesis value contradicts the estimate of less than 'withdrawal_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the withdrawal amount
    # any amount of withdrawal less than 'withdrawal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
