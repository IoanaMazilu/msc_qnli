total_hours_premise = 61
total_hours_hypothesis = 41

# the hypothesis talks about the number of hours worked by James last week, referenced also in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
