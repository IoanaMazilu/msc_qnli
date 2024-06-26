ratio_premise = 6/7
ratio_hypothesis = 1/7

horse_food_premise = 230
horse_food_hypothesis = 230
total_horse_food_premise = 12880
total_horse_food_hypothesis = 12880

# the hypothesis refers to the ratio between the number of sheep and the number of horses and the amount of food each horse eats
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_hypothesis!= horse_food_premise:
    # check if the amount of food each horse eats in the hypothesis contradicts the amount of food each horse eats in the premise
    label = "contradiction"
elif total_horse_food_hypothesis!= total_horse_food_premise:
    # check if the total amount of food the farm needs in the hypothesis contradicts the total amount of food the farm needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
