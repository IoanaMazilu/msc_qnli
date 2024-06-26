ratio_sheep_horses_premise = 5/7
horse_food_per_horse = 230
total_horse_food_premise = 12880
ratio_sheep_horses_hypothesis = 5/7 + 0.01 # the hypothesis ratio is more than 5 to 7, so we add a small value to it

# the number of horses in the premise can be calculated by dividing the total horse food by the food needed per horse
horses_premise = total_horse_food_premise / horse_food_per_horse

# the number of sheep in the premise can be calculated by multiplying the number of horses by the ratio
sheep_premise = horses_premise * ratio_sheep_horses_premise

# similarly, the number of sheep in the hypothesis can be calculated
sheep_hypothesis = horses_premise * ratio_sheep_horses_hypothesis

# the hypothesis refers to the number of sheep and horses in the premise
if sheep_hypothesis < sheep_premise:
    # check if the number of sheep in the hypothesis contradicts the number of sheep in the premise
    label = "contradiction"
else:
    # the premise gives an exact ratio between the number of sheep and horses
    # any ratio more than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
