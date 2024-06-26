# define variables for the numerical entities in the premise
sheep_horses_ratio_premise = 1
sheep_horses_ratio_hypothesis = 6
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230
total_horse_food_premise = 12880
total_horse_food_hypothesis = 12880

# check if the ratio between the number of sheep and the number of horses in the hypothesis contradicts the ratio in the premise
if sheep_horses_ratio_hypothesis <= sheep_horses_ratio_premise:
    label = "contradiction"
else:
    # check if the number of horses in the hypothesis contradicts the number of horses in the premise
    if horse_food_per_day_hypothesis!= horse_food_per_day_premise:
        label = "contradiction"
    elif total_horse_food_hypothesis!= total_horse_food_premise:
        label = "contradiction"
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"

print(label)
