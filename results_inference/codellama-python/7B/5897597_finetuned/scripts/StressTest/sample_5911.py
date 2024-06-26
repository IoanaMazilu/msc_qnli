ratio_sheep_horses_premise = 6/7
ratio_sheep_horses_hypothesis = 1/7
horse_food_per_day = 230
total_food_needed = 12880

# the hypothesis refers to the ratio of sheep to horses and the amount of food per day for horses, both mentioned in the premise
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio of sheep to horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_per_day!= horse_food_per_day or total_food_needed!= total_food_needed:
    # check if the amount of food per day for horses or the total food needed for the farm in the hypothesis contradicts the values in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of sheep to horses
    # any ratio less than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
