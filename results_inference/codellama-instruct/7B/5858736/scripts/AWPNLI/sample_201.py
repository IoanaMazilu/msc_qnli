seats_premise = 14.0
people_per_seat = 6.0
total_people_premise = seats_premise * people_per_seat
if total_people_hypothesis >= total_people_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
