# Premise: About one in five white and African-American women and one in seven Hispanic women reported being raped at some point.
# Hypothesis: Nearly 1 in 5 women report being raped in their lifetime.
# Golden Label: neutral

rape_ratio_white_afro_women_premise = 1/5
rape_ratio_hispanic_women_premise = 1/7
rape_ratio_women_hypothesis = 1/5

# the hypothesis mentions the rape ratio for women in general, which is also mentioned in the premise
# however, the premise provides specific ratios for white, African-American, and Hispanic women,
# which cannot be directly compared with the general ratio mentioned in the hypothesis
label = "neutral"

print(label)

