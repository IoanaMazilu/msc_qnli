# define the variables from the premise
ratio_sheep_horses_premise = 2/7
horse_food_per_day_premise = 230
total_horse_food_per_day_premise = 12880

# define the variables from the hypothesis
ratio_sheep_horses_hypothesis = 2/7
horse_food_per_day_hypothesis = 230
total_horse_food_per_day_hypothesis = 12880

# calculate the number of horses based on the horse food consumed
horses_premise = total_horse_food_per_day_premise / horse_food_per_day_premise
horses_hypothesis = total_horse_food_per_day_hypothesis / horse_food_per_day_hypothesis

# the hypothesis refers to the same ratio and the same amount of horse food consumption as in the premise
if ratio_sheep_horses_hypothesis < ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horses_hypothesis != horses_premise:
    # check if the number of horses calculated in the hypothesis contradicts the number of horses calculated in the premise
    label = "contradiction"
else:
    # if the ratio and the number of horses do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
