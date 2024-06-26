sheep_to_horses_ratio_premise = 6/7
sheep_to_horses_ratio_hypothesis = 6/7
total_horses_premise = 7
total_horses_hypothesis = 7
total_food_premise = 12880
total_food_hypothesis = 12880

# the hypothesis refers to the same ratios and numbers mentioned in the premise
if sheep_to_horses_ratio_premise!= sheep_to_horses_ratio_hypothesis:
    # check if the ratio between sheep and horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif total_horses_premise!= total_horses_hypothesis:
    # check if the number of horses in the hypothesis contradicts the number of horses in the premise
    label = "contradiction"
elif total_food_premise!= total_food_hypothesis:
    # check if the total amount of food in the hypothesis contradicts the total amount of food in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
