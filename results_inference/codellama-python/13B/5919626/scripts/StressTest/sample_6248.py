amount_premise = 100000
amount_hypothesis = 100000

# the hypothesis talks about the amount of money invested by Raviraj, which is the same as the amount of money invested in the premise
if amount_premise!= amount_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money invested
    # any amount of money invested is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
