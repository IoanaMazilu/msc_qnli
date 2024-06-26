years_premise = 6
age_premise = 30
years_hypothesis = 6
age_hypothesis = 30

# the hypothesis speaks about the same time frame and age as the premise
if years_hypothesis >= years_premise:
    # check if the time frame contradicts the premise
    label = "contradiction"
elif age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of years and the age
    # any lower number of years is inconsistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
