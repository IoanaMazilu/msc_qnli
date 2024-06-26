age_after_years_premise = 38
years_after_premise = 6
age_after_years_hypothesis = 38
years_after_hypothesis = 4

# the hypothesis refers to the age of Sandy after a number of years, which is also mentioned in the premise
if age_after_years_hypothesis!= age_after_years_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif years_after_hypothesis >= years_after_premise:
    # check if the number of years in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of years until Sandy's age, 
    # any number of years less than 'years_after_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
