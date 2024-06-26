y_premise = 22500
y_hypothesis = 62500

# the hypothesis talks about the amount Lucy deposited in an investment fund, which is also mentioned in the premise
if y_hypothesis <= y_premise:
    # check if the value in the hypothesis contradicts the estimate of more than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit amount
    # any deposit amount greater than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
