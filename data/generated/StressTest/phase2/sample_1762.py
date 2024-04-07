# Premise: The ratio of men to women in the Snyder community choir is less than 7 to 3.
# Hypothesis: The ratio of men to women in the Snyder community choir is 4 to 3.
# Golden Label: neutral

men_women_ratio_premise = 7 / 3
men_women_ratio_hypothesis = 4 / 3

# the hypothesis refers to the men to women ratio in the choir, mentioned also in the premise
if men_women_ratio_hypothesis >= men_women_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimation of less than 'men_women_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'men_women_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

