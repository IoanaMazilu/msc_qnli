ayisha_age_ratio_premise = 1/6
ayisha_age_ratio_hypothesis = 1/6

# the hypothesis talks about the ratio of Ayisha's age to her father's age, referenced also in the premise
if ayisha_age_ratio_hypothesis >= ayisha_age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ayisha_age_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of Ayisha's age to her father's age
    # any ratio less than 'ayisha_age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
