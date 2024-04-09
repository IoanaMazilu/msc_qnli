west_town_to_east_town_premise = 85
west_town_to_east_town_hypothesis = 15

# the hypothesis talks about the distance between West-Town and East-Town
if west_town_to_east_town_hypothesis <= west_town_to_east_town_premise:
    # check if the hypothesis value contradicts the estimate of less than 'west_town_to_east_town_premise'
    label = "contradiction"
else:
    # the premise gives a specific value for the distance, while the hypothesis gives a different value
    # any distance less than 85 kilometers is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
