# Premise: The ratio between the number of sheep and the number of horses at the Stewart farm is 2 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?
# Hypothesis: The ratio between the number of sheep and the number of horses at the Stewart farm is less than 5 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?
# Golden Label: entailment

# Variables for premise
ratio_sheep_horses_premise = 2 / 7
food_per_horse = 230
total_horse_food = 12880

# Variables for hypothesis
ratio_sheep_horses_hypothesis = 5 / 7

# Calculating the number of horses from the total horse food
number_of_horses = total_horse_food / food_per_horse

# the hypothesis talks about the ratio of sheep to horses at the same farm, referenced also in the premise
if ratio_sheep_horses_hypothesis > ratio_sheep_horses_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_sheep_horses_premise'
    label = "contradiction"
elif ratio_sheep_horses_hypothesis == ratio_sheep_horses_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the ratio of sheep to horses
    # any ratio less than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

