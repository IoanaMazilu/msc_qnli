# define variables for the numerical entities in the premise
sheep_farm_premise = 6
horses_farm_premise = 7
horse_food_premise = 230
total_horse_food_premise = 12880

# define variables for the numerical entities in the hypothesis
sheep_farm_hypothesis = 1
horses_farm_hypothesis = 7
horse_food_hypothesis = 230
total_horse_food_hypothesis = 12880

# calculate the ratio of sheep to horses in the premise
ratio_premise = sheep_farm_premise / horses_farm_premise

# calculate the ratio of sheep to horses in the hypothesis
ratio_hypothesis = sheep_farm_hypothesis / horses_farm_hypothesis

# check if the ratio in the hypothesis contradicts the ratio in the premise
if ratio_hypothesis!= ratio_premise:
    label = "contradiction"
else:
    # if the ratio in the hypothesis is consistent with the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
