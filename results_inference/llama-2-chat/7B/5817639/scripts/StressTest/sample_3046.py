days_per_week_premise = 5
days_per_week_hypothesis = 8

# the hypothesis talks about the number of hours Sheila works per day on each day of the week, referenced also in the premise
if days_per_week_hypothesis <= days_per_week_premise:
    # check if the hypothesis value contradicts the estimate of 'days_per_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Sheila works per day on each day of the week
    # any number of hours greater than 'days_per_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
