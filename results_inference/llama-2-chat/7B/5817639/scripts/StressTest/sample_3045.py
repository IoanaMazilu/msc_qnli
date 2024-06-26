day_hours_premise = {
    "Monday": 8,
    "Wednesday": 8,
    "Friday": 8,
    "Tuesday": 6,
    "Thursday": 6
}

day_hours_hypothesis = {
    "Monday": 5,
    "Wednesday": 5,
    "Friday": 5,
    "Tuesday": 6,
    "Thursday": 6
}

# the hypothesis talks about the number of hours Sheila works per day, referenced also in the premise
for day in day_hours_premise:
    if day_hours_hypothesis[day] <= day_hours_premise[day]:
        # check if the hypothesis value contradicts the estimate of 'day_hours_premise[day]'
        label = "contradiction"
    else:
        # the premise gives only an estimate for the number of hours Sheila works per day
        # any number of hours greater than 'day_hours_premise[day]' is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"

print(label)
