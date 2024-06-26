total_amount_premise = 500
total_amount_hypothesis = 600

# the hypothesis refers to the total amount and the share of Greg, both mentioned in the premise
if total_amount_premise <= total_amount_hypothesis:
    # check if the estimate of 'total_amount_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount
    # any total amount greater than 'total_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
