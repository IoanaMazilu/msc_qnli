# define variables for the numerical entities in the premise
sheep_horses_ratio_premise = 6
sheep_horses_ratio_hypothesis = 7
horse_food_per_day_premise = 230
horse_food_per_day_hypothesis = 230
total_horse_food_premise = 12880
total_horse_food_hypothesis = 12880

# extract the quantities as valid numbers
sheep_horses_ratio_premise = int(sheep_horses_ratio_premise)
sheep_horses_ratio_hypothesis = int(sheep_horses_ratio_hypothesis)
horse_food_per_day_premise = int(horse_food_per_day_premise)
horse_food_per_day_hypothesis = int(horse_food_per_day_hypothesis)
total_horse_food_premise = int(total_horse_food_premise)
total_horse_food_hypothesis = int(total_horse_food_hypothesis)

# perform calculations if necessary
total_sheep_food_premise = horse_food_per_day_premise * sheep_horses_ratio_premise
total_sheep_food_hypothesis = horse_food_per_day_hypothesis * sheep_horses_ratio_hypothesis

# compare the quantities to infer the label
if total_sheep_food_premise <= total_sheep_food_hypothesis:
    # check if the estimate of 'total_sheep_food_hypothesis' contradicts the number of sheep in the premise
    label = "contradiction"
elif total_sheep_food_hypothesis!= total_sheep_food_premise:
    # check if the number of sheep in the hypothesis contradicts the number of sheep reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
