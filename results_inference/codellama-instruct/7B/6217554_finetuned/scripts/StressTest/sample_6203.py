travel_distance_premise = 200
travel_distance_hypothesis = 200

if travel_distance_hypothesis <= travel_distance_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
