work_hours_per_day = {
    "Monday": 8,
    "Wednesday": 8,
    "Friday": 8,
    "Tuesday": 6,
    "Thursday": 6
}

# the hypothesis talks about the number of hours Sheila works per day on different days
# the premise provides the number of hours Sheila works per day on different days
# we can now check if the number of hours in the hypothesis contradicts or is consistent with the number of hours in the premise
if work_hours_per_day!= {day: work_hours_per_day[day] for day in work_hours_per_day}:
    label = "contradiction"
else:
    label = "entailment"

print(label)
