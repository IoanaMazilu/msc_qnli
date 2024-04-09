ayisha_age_fraction_premise = 1/6
ayisha_age_fraction_hypothesis = 1/6

# the hypothesis refers to Ayisha's age fraction in relation to her father's age, also mentioned in the premise
if ayisha_age_fraction_hypothesis >= ayisha_age_fraction_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
