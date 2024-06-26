distance_west_town_east_town_premise = 85
distance_west_town_east_town_hypothesis = 15

if distance_west_town_east_town_hypothesis <= distance_west_town_east_town_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
