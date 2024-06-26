ratio_sheep_horses_premise = 1/7
ratio_sheep_horses_hypothesis = 6/7
horse_food_per_day = 230
total_horse_food_needed = 12880

# the hypothesis talks about the ratio between the number of sheep and horses and the amount of food each horse eats
# the premise also gives this information
if ratio_sheep_horses_premise >= ratio_sheep_horses_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
