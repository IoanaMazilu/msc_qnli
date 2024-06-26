years_until_age_30_premise = 6
years_until_age_30_hypothesis = 2
age_after_years_premise = 30
age_after_years_hypothesis = 30

# the hypothesis refers to the number of years until Sandy turns 30, which is also mentioned in the premise
if years_until_age_30_hypothesis >= years_until_age_30_premise:
    # check if the hypothesis value contradicts the number of years until Sandy turns 30 in the premise
    label = "contradiction"
elif age_after_years_hypothesis!= age_after_years_premise:
    # check if the age after the number of years in the hypothesis contradicts the age after the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
