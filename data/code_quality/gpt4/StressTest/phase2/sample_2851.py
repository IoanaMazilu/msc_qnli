hourly_rate_premise = 10.00
hourly_rate_hypothesis = 10.00
working_hours_premise = 10
working_hours_hypothesis = 40

# the hypothesis talks about the earnings and working hours of Winson, referenced also in the premise
if hourly_rate_hypothesis != hourly_rate_premise:
    # check if the hourly rate in the hypothesis contradicts the hourly rate mentioned in the premise
    label = "contradiction"
elif working_hours_hypothesis <= working_hours_premise:
    # check if the working hours in the hypothesis contradicts the estimate of more than 'working_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the working hours
    # any number of working hours greater than 'working_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
