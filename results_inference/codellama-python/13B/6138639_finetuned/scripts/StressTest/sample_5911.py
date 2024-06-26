sheep_to_horses_ratio_premise = 6/7
sheep_to_horses_ratio_hypothesis = 1/7
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230
total_horse_food_per_day_premise = 12880
total_horse_food_per_day_hypothesis = 12880

# the hypothesis talks about the ratio between the number of sheep and the number of horses, referenced also in the premise
if sheep_to_horses_ratio_hypothesis >= sheep_to_horses_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than'sheep_to_horses_ratio_premise'
    label = "contradiction"
elif horse_food_per_day_hypothesis!= horse_food_per_day_premise:
    # check if the amount of horse food per day in the hypothesis contradicts the amount of horse food per day reported in the premise
    label = "contradiction"
elif total_horse_food_per_day_hypothesis!= total_horse_food_per_day_premise:
    # check if the total amount of horse food per day in the hypothesis contradicts the total amount of horse food per day reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the number of sheep and the number of horses
    # any ratio less than'sheep_to_horses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
