# Premise: Ayisha's age is 1/6 th of her father's age.
# Hypothesis: Ayisha's age is less than 1/6 th of her father's age.
# Golden Label: contradiction

ayisha_age_ratio_premise = 1/6
ayisha_age_ratio_hypothesis = 1/6

# the hypothesis talks about the ratio of Ayisha's age to her father's age, as referenced in the premise
if ayisha_age_ratio_hypothesis == ayisha_age_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio given in the premise
    label = "contradiction"
elif ayisha_age_ratio_hypothesis < ayisha_age_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio given in the premise
    label = "contradiction"
else:
    # the premise gives an exact ratio for Ayisha's age to her father's age
    # any ratio equal or greater than 'ayisha_age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

