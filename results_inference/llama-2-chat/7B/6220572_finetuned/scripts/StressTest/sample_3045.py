hours_per_day_monday_wednesday_friday_hypothesis = 5
hours_per_day_tuesday_thursday_hypothesis = 6

# the hypothesis talks about the number of hours worked per day, referenced also in the premise
if hours_per_day_monday_wednesday_friday_hypothesis <= hours_per_day_tuesday_thursday_hypothesis:
    # check if the hypothesis value contradicts the number of hours worked per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per day
    # any number of hours greater than 'hours_per_day_tuesday_thursday_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
