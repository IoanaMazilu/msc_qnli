total_hours_premise = 41
total_hours_hypothesis = 51

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if total_hours_hypothesis <= total_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours greater than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
