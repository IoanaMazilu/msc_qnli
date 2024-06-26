y_premise = 72500
y_hypothesis = 62500

# the hypothesis talks about the amount Lucy deposited, which is also referenced in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the estimate of less than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit amount
    # any deposit amount less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
