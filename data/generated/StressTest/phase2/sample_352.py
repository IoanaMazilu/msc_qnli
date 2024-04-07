# Premise: The ratio of men to women in the Snyder community choir is more than 2 to 7.
# Hypothesis: The ratio of men to women in the Snyder community choir is 4 to 7.
# Golden Label: neutral

men_women_ratio_premise = 2/7
men_women_ratio_hypothesis = 4/7

# the hypothesis refers to the ratio of men to women in the Snyder community choir mentioned in the premise
if men_women_ratio_hypothesis <= men_women_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'men_women_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of men to women
    # any ratio greater than 'men_women_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

