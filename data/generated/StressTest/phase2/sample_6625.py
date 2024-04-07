# Premise: The ratio between the number of sheep and the number of horses at the Stewart farm is more than 1 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?
# Hypothesis: The ratio between the number of sheep and the number of horses at the Stewart farm is 6 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?
# Golden Label: neutral

# defining the numerical entities
sheep_horse_ratio_premise = 1/7
sheep_horse_ratio_hypothesis = 6/7
horse_food_per_day = 230
total_horse_food = 12880

# the hypothesis talks about the ratio of the number of sheep to the number of horses at the same farm
if sheep_horse_ratio_hypothesis <= sheep_horse_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'sheep_horse_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the number of sheep to the number of horses
    # any ratio greater than 'sheep_horse_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

