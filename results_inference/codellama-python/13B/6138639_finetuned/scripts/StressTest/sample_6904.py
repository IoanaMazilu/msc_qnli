total_paid_premise = 360
total_paid_hypothesis = 160

# the hypothesis talks about the total amount paid by Rahul, which is also mentioned in the premise
if total_paid_hypothesis >= total_paid_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_paid_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount paid
    # any amount less than 'total_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
