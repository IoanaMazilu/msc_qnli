ratio_sheep_horses_premise = 1/7
ratio_sheep_horses_hypothesis = 6/7
horse_food_per_day = 230
total_horse_food_needed = 12880

# the hypothesis refers to the ratio of sheep to horses and the amount of horse food needed at the farm, both mentioned in the premise
if ratio_sheep_horses_hypothesis <= ratio_sheep_horses_premise:
    # check if the ratio of sheep to horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_per_day!= horse_food_per_day or total_horse_food_needed!= total_horse_food_needed:
    # check if the amount of horse food needed per day or the total amount of horse food needed contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of sheep to horses
    # any ratio greater than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
