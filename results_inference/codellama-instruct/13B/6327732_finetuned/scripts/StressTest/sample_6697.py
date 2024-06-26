withdrawal_premise = 5000
withdrawal_hypothesis = 2000

# the hypothesis refers to the amount withdrawn by Tony, which is mentioned in the premise
if withdrawal_hypothesis >= withdrawal_premise:
    # check if the hypothesis value contradicts the estimate of less than 'withdrawal_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount withdrawn
    # any amount less than 'withdrawal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
