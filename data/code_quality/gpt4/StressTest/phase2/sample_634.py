hourly_rate_premise = 7.00
hourly_rate_hypothesis = 7.00
hours_premise = 80
hours_hypothesis = 40

# the hypothesis talks about the hourly rate and hours worked per week, referenced also in the premise
if hourly_rate_hypothesis != hourly_rate_premise:
    # check if the hourly rate in the hypothesis contradicts the hourly rate in the premise
    label = "contradiction"
elif hours_hypothesis >= hours_premise:
    # check if the hours worked per week in the hypothesis contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the hours worked per week
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
