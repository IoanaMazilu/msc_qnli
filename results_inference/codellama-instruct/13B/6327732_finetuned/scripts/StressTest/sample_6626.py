# define variables for the numerical entities in the premise
sheep_farm_premise = 6
horses_farm_premise = 7
horse_food_premise = 230
total_horse_food_premise = 12880

# define variables for the numerical entities in the hypothesis
sheep_farm_hypothesis = 7
horses_farm_hypothesis = 6
horse_food_hypothesis = 230
total_horse_food_hypothesis = 12880

# check if the ratio of sheep to horses in the hypothesis contradicts the ratio in the premise
if sheep_farm_hypothesis * horses_farm_hypothesis < sheep_farm_premise * horses_farm_premise:
    label = "contradiction"

# check if the total amount of horse food in the hypothesis contradicts the total amount in the premise
elif total_horse_food_hypothesis!= total_horse_food_premise:
    label = "contradiction"

# if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
