ratio_sheep_horses_premise = 6/7
ratio_sheep_horses_hypothesis = 1/7
horse_food_per_day = 230
total_horse_food_needed = 12880

# the hypothesis refers to the ratio between the number of sheep and horses, the amount of food each horse eats and the total food needed as in the premise
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'ratio_sheep_horses_premise'
    label = "contradiction"
elif horse_food_per_day!= 230 or total_horse_food_needed!= 12880:
    # check if the amount of food each horse eats or the total food needed contradicts the amounts reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the number of sheep and horses
    # any ratio less than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
