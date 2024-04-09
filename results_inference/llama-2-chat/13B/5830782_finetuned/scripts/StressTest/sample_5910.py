ratio_sheep_horses_premise = 1/7
ratio_sheep_horses_hypothesis = 6/7
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230
total_horse_food_needed_premise = 12880
total_horse_food_needed_hypothesis = 12880

# the hypothesis talks about the ratio between the number of sheep and the number of horses, the amount of food each horse eats and the total amount of food needed for the horses, all referenced also in the premise
if ratio_sheep_horses_hypothesis <= ratio_sheep_horses_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_sheep_horses_premise'
    label = "contradiction"
elif horse_food_per_day_hypothesis!= horse_food_per_day_premise:
    # check if the amount of food each horse eats in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif total_horse_food_needed_hypothesis!= total_horse_food_needed_premise:
    # check if the total amount of food needed for the horses in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
