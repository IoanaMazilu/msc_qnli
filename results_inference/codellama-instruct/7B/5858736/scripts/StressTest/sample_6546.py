distance_west_town_east_town_premise = 15
distance_west_town_east_town_hypothesis = 85

if distance_west_town_east_town_hypothesis <= distance_west_town_east_town_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
