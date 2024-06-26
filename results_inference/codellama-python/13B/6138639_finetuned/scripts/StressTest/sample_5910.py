sheep_to_horses_ratio_premise = 1/7
sheep_to_horses_ratio_hypothesis = 6/7

horse_food_per_day = 230
total_food_needed = 12880

# the hypothesis refers to the ratio between the number of sheep and the number of horses at the farm, as well as the amount of food needed per day
if sheep_to_horses_ratio_hypothesis <= sheep_to_horses_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives the exact ratio between the number of sheep and the number of horses
    # any ratio less than'sheep_to_horses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
