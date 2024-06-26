ayisha_age_fraction_premise = 3/6
ayisha_age_fraction_hypothesis = 1/6

# the hypothesis refers to the fraction of Ayisha's age compared to her father's age mentioned in the premise
if ayisha_age_fraction_hypothesis >= ayisha_age_fraction_premise:
    # check if the fraction of 'ayisha_age_fraction_hypothesis' contradicts the fraction of Ayisha's age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of Ayisha's age compared to her father's age
    # any fraction less than 'ayisha_age_fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
