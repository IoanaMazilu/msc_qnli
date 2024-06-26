ratio_sheep_horses_premise = 1/7
ratio_sheep_horses_hypothesis = 6/7
horse_food_per_day = 230
total_horse_food_needed = 12880

# the hypothesis refers to the ratio between the number of sheep and horses, the amount of food each horse eats and the total food needed as in the premise
if ratio_sheep_horses_hypothesis <= ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_per_day!= 230 or total_horse_food_needed!= 12880:
    # check if the amount of food each horse eats or the total food needed contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
