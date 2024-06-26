hourly_rate_premise = 7.00
weekly_hours_premise = 40
hourly_rate_hypothesis = 7.00
weekly_hours_hypothesis = 40

# the hypothesis talks about the hourly rate and number of hours Edward works per week, which is also mentioned in the premise
if hourly_rate_hypothesis != hourly_rate_premise:
    # check if the hourly rate in the hypothesis contradicts the hourly rate mentioned in the premise
    label = "contradiction"
elif weekly_hours_hypothesis <= weekly_hours_premise:
    # check if the number of hours Edward works per week in the hypothesis contradicts the number of hours mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of hours Edward works per week
    # any number of hours more than 'weekly_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
