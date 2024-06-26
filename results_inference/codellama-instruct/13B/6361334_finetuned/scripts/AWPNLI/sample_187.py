num_boats_premise = 5.0
num_people_per_boat_premise = 3.0
total_people_premise = num_boats_premise * num_people_per_boat_premise

num_people_hypothesis = 19.0

if num_people_hypothesis!= total_people_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
