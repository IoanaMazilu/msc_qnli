premise_amount = 1300
hypothesis_amount = <less than 1300>

# the hypothesis refers to the amount of Deepak's share
if premise_amount <= hypothesis_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount of Deepak's share in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of Deepak's share
    # any amount less than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
