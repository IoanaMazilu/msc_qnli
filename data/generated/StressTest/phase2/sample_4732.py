# Premise: The ratio of men to women in the Snyder community choir is more than 3 to 5.
# Hypothesis: The ratio of men to women in the Snyder community choir is 6 to 5.
# Golden Label: neutral

men_women_ratio_premise = 3 / 5
men_women_ratio_hypothesis = 6 / 5

# the hypothesis refers to the ratio of men to women in the choir, which is also mentioned in the premise
if men_women_ratio_hypothesis <= men_women_ratio_premise:
    # check if the hypothesis ratio contradicts the premise saying the ratio is more than 'men_women_ratio_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio
    # any ratio greater than 'men_women_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

