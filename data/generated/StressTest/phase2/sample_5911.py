# Premise: The ratio between the number of sheep and the number of horses at the Stewart farm is less than 6 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?
# Hypothesis: The ratio between the number of sheep and the number of horses at the Stewart farm is 1 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?
# Golden Label: neutral

ratio_premise = 6 / 7
ratio_hypothesis = 1 / 7

# the hypothesis talks about the ratio between the number of sheep and horses at the Stewart farm, referenced also in the premise
if ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # check if the ratio in the hypothesis entail the ratio in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the ratio
    # any ratio which is less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

