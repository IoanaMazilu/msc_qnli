# Premise: If Anup is less than 6 years younger to Madan whose age is 5 yrs, then whatis John’s present age?
# Hypothesis: If Anup is 2 years younger to Madan whose age is 5 yrs, then whatis John’s present age?
# Golden Label: neutral

madan_age_premise = 5
anup_age_difference_premise = 6
madan_age_hypothesis = 5
anup_age_difference_hypothesis = 2

# the hypothesis speaks about the ages of Madan and Anup, which are also mentioned in the premise
if madan_age_premise != madan_age_hypothesis:
    # check if the age of Madan in the hypothesis contradicts the age in the premise
    label = "contradiction"
elif anup_age_difference_hypothesis >= anup_age_difference_premise:
    # check if the age difference between Anup and Madan in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # the premise gives a maximum difference for the age of Anup relative to Madan
    # any difference smaller than 'anup_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

