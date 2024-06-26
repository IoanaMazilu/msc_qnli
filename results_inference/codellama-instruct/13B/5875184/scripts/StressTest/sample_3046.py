premise_hours_per_day = {
    "Monday": 5,
    "Wednesday": 5,
    "Friday": 5,
    "Tuesday": 6,
    "Thursday": 6
}

hypothesis_hours_per_day = {
    "Monday": 8,
    "Wednesday": 8,
    "Friday": 8,
    "Tuesday": 6,
    "Thursday": 6
}

# check if the hypothesis values contradict the premise ones
if hypothesis_hours_per_day["Monday"] <= premise_hours_per_day["Monday"]:
    label = "contradiction"
elif hypothesis_hours_per_day["Wednesday"] <= premise_hours_per_day["Wednesday"]:
    label = "contradiction"
elif hypothesis_hours_per_day["Friday"] <= premise_hours_per_day["Friday"]:
    label = "contradiction"
elif hypothesis_hours_per_day["Tuesday"]!= premise_hours_per_day["Tuesday"]:
    label = "contradiction"
elif hypothesis_hours_per_day["Thursday"]!= premise_hours_per_day["Thursday"]:
    label = "contradiction"
else:
    label = "entailment"

print(label)
