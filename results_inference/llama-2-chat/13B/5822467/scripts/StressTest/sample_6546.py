west_town_to_east_town_premise = 15
west_town_to_east_town_hypothesis = 85

# the hypothesis refers to the distance between West-Town and East-Town
if west_town_to_east_town_hypothesis <= west_town_to_east_town_premise:
    # check if the hypothesis value contradicts the estimate of the distance in the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the distance, any value less than that is consistent with the premise
    label = "neutral"

print(label)
