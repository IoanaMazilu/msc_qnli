ratio_sheep_horses_premise = 6 / 7
ratio_sheep_horses_hypothesis = 6 / 7

horse_food_per_day = 230
total_horse_food_needed = 12880

# the hypothesis refers to the ratio between the number of sheep and horses, the amount of food each horse eats and the total food needed
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the number of sheep to horses
    # any ratio less than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
