john_age_in_5_years_premise = 5
john_age_in_8_years_hypothesis = 8

# the hypothesis refers to John's age in a certain number of years, which is also mentioned in the premise
if john_age_in_8_years_hypothesis >= john_age_in_5_years_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
