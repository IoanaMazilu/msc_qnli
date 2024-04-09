sheep_ratio_premise = 1.05
sheep_ratio_hypothesis = 6.0
horse_food_premise = 12880
horse_food_hypothesis = 12880

# the hypothesis talks about the ratio of sheep to horses in the farm, which is consistent with the premise
if sheep_ratio_hypothesis <= sheep_ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of sheep to horses
    # any ratio greater than or equal to the premise ratio is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# calculate the number of sheep in the farm based on the hypothesis ratio
sheep_count = (sheep_ratio_hypothesis * horse_food_hypothesis) / (1 + sheep_ratio_hypothesis)

print(label)
print("The number of sheep in the farm is:", sheep_count)
