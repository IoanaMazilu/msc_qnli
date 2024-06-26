mary_age_factor_premise = 6
mary_age_factor_hypothesis = 2
betty_age_factor_premise = 4
betty_age_factor_hypothesis = 4

# the hypothesis talks about the relationship of Albert's age with Mary's and Betty's ages, referenced also in the premise
if mary_age_factor_hypothesis >= mary_age_factor_premise:
    # check if the hypothesis value contradicts the estimate of less than 'mary_age_factor_premise'
    label = "contradiction"
elif betty_age_factor_hypothesis != betty_age_factor_premise:
    # check if the relation of Albert's age with Betty's age in the hypothesis contradicts the relation reported in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the factor of Mary's age
    # any number less than 'mary_age_factor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
