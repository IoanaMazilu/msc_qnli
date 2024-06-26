ayisha_age_ratio_premise = 3/6
ayisha_age_ratio_hypothesis = 1/6

# the hypothesis refers to Ayisha's age ratio to her father's age, which is also mentioned in the premise
if ayisha_age_ratio_hypothesis >= ayisha_age_ratio_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'ayisha_age_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Ayisha's age ratio
    # any ratio less than 'ayisha_age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
