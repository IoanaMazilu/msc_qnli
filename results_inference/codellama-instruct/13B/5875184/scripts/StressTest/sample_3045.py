premise_hours_per_day = {
    "Monday": 8,
    "Wednesday": 8,
    "Friday": 8,
    "Tuesday": 6,
    "Thursday": 6
}
hypothesis_hours_per_day = {
    "Monday": 5,
    "Wednesday": 5,
    "Friday": 5,
    "Tuesday": 6,
    "Thursday": 6
}

# check if the hypothesis values contradict the premise ones
for day in premise_hours_per_day:
    if hypothesis_hours_per_day[day] > premise_hours_per_day[day]:
        label = "contradiction"
        break
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
