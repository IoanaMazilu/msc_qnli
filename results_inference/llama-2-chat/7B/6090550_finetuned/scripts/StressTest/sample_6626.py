sheep_horses_premise = 6/7
sheep_horses_hypothesis = 6/7
horse_food_premise = 230
horse_food_hypothesis = 230
total_food_premise = 12880
total_food_hypothesis = 12880

# the hypothesis talks about the same ratios and quantities as the premise
if sheep_horses_premise!= sheep_horses_hypothesis:
    # check if the ratio between sheep and horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif horse_food_hypothesis!= horse_food_premise:
    # check if the amount of horse food per day in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif total_food_hypothesis!= total_food_premise:
    # check if the total amount of food in the hypothesis contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
