ratio_sheep_horses_premise = 5/7
ratio_sheep_horses_hypothesis = 2/7
horse_food_per_horse = 230
total_horse_food_premise = 12880
total_horse_food_hypothesis = 12880

# the hypothesis refers to the ratio of the number of sheep to horses and the amount of horse food, which are also mentioned in the premise

if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio of sheep to horses in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif total_horse_food_hypothesis != total_horse_food_premise:
    # check if the total amount of horse food in the hypothesis contradicts the total amount of horse food mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
