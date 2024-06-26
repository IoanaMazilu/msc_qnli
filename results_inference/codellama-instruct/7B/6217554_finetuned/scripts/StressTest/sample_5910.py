# define variables for the premise
sheep_horses_ratio_premise = 1/7
horse_food_per_day_premise = 230
total_food_per_day_premise = 12880

# define variables for the hypothesis
sheep_horses_ratio_hypothesis = 6/7

# check if the hypothesis ratio contradicts the premise one
if sheep_horses_ratio_hypothesis >= sheep_horses_ratio_premise:
    # check if the hypothesis ratio contradicts the premise one
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sheep
    # any number of sheep greater than'sheep_horses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
