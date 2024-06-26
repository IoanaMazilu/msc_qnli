ratio_sheep_horses_premise = 1/7
ratio_sheep_horses_hypothesis = 6/7
horse_food_per_day = 230
total_horse_food_needed = 12880

# the hypothesis refers to the ratio between the number of sheep and the number of horses, as well as the amount of food each horse eats and the total food needed, all mentioned in the premise
if ratio_sheep_horses_hypothesis <= ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_per_day!= 230 or total_horse_food_needed!= 12880:
    # check if the quantities of food per day in the hypothesis contradict the quantities of food per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the number of sheep and the number of horses
    # any ratio greater than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
