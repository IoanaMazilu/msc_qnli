ratio_sheep_horses_premise = 6/7
ratio_sheep_horses_hypothesis = 6/7
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230
total_food_needed_premise = 12880
total_food_needed_hypothesis = 12880

# the hypothesis refers to the ratio of sheep to horses, the amount of food per horse and the total food needed, all mentioned in the premise
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio of sheep to horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_per_day_hypothesis!= horse_food_per_day_premise:
    # check if the amount of food per horse in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif total_food_needed_hypothesis!= total_food_needed_premise:
    # check if the total food needed in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
