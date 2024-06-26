sheep_horses_ratio_premise = 6/7
sheep_horses_ratio_hypothesis = 6/7
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230
total_horse_food_premise = 12880
total_horse_food_hypothesis = 12880

# the hypothesis refers to the ratio between sheep and horses, the amount of food for horses, and the total food needed, all mentioned in the premise
if sheep_horses_ratio_hypothesis >= sheep_horses_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_per_day_hypothesis!= horse_food_per_day_premise:
    # check if the amount of food for horses in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif total_horse_food_hypothesis!= total_horse_food_premise:
    # check if the total food needed in the hypothesis contradicts the total food needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
