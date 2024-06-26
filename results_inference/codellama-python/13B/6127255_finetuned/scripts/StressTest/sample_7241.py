ayisha_age_factor_premise = 1/6
ayisha_age_factor_hypothesis = 1/6

# the hypothesis refers to the factor of Ayisha's age in relation to her father's age mentioned in the premise
if ayisha_age_factor_hypothesis >= ayisha_age_factor_premise:
    # check if the factor of 'ayisha_age_factor_hypothesis' contradicts the factor of Ayisha's age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
