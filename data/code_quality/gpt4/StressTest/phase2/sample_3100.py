years_to_double_age_premise = 30
years_to_double_age_hypothesis = 10

# the hypothesis refers to the number of years until Souju's father's age will be twice Tharak's age
if years_to_double_age_hypothesis >= years_to_double_age_premise:
    # check if 'years_to_double_age_hypothesis' contradicts the estimate of less than 'years_to_double_age_premise'
    label = "contradiction"
elif years_to_double_age_hypothesis < years_to_double_age_premise:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'years_to_double_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
