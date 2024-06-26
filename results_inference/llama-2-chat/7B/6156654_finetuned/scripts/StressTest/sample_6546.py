distance_west_town_east_town = 15
distance_hypothesis = 85

# the hypothesis refers to the distance between West-Town and East-Town
if distance_west_town_east_town >= distance_hypothesis:
    # if the distance between West-Town and East-Town is greater than or equal to the hypothesis, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance between West-Town and East-Town is less than the hypothesis, it contradicts the hypothesis
    label = "contradiction"

print(label)
