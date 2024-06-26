total_amount_premise = 600
total_amount_hypothesis = 500

# the hypothesis refers to the total amount and the share of Greg
if total_amount_hypothesis <= total_amount_premise:
    # check if the estimate of 'total_amount_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount
    # any total amount greater than 'total_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
