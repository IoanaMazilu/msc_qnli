first_hours_paid_premise = 20
first_hours_paid_hypothesis = 30

# The hypothesis talks about the number of hours Harry is paid x dollars per hour, referenced also in the premise
if first_hours_paid_hypothesis <= first_hours_paid_premise:
    # Check if the hypothesis value contradicts the premise, because the premise talks about more than 'first_hours_paid_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate (more than 'first_hours_paid_premise') for the number of hours Harry is paid x dollars per hour
    # Any number of hours greater than 'first_hours_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
