boats_premise = 5.0
people_per_boat_premise = 3.0
total_people_premise = boats_premise * people_per_boat_premise

hypothesis_people = 15.0

if total_people_premise!= hypothesis_people:
    label = "contradiction"
else:
    label = "entailment"

print(label)
