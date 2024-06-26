total_paid_premise = 160
total_paid_hypothesis = 360

# the hypothesis talks about the total amount paid to rent the tool, referenced also in the premise
if total_paid_hypothesis <= total_paid_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_paid_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount paid
    # any total amount greater than 'total_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
