# define variables for the numerical entities in the premise
sheep_farm_premise = 1
horses_farm_premise = 7
sheep_farm_hypothesis = 6
horses_farm_hypothesis = 7

# extract quantities as valid numbers
sheep_farm_premise = int(sheep_farm_premise)
horses_farm_premise = int(horses_farm_premise)
sheep_farm_hypothesis = int(sheep_farm_hypothesis)
horses_farm_hypothesis = int(horses_farm_hypothesis)

# perform calculations
total_horse_food_premise = 12880
total_horse_food_hypothesis = 12880
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230

# check if the hypothesis values contradict the premise ones
if sheep_farm_hypothesis!= sheep_farm_premise:
    label = "contradiction"
elif horses_farm_hypothesis!= horses_farm_premise:
    label = "contradiction"
elif total_horse_food_hypothesis!= total_horse_food_premise:
    label = "contradiction"
elif horse_food_per_day_hypothesis!= horse_food_per_day_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
