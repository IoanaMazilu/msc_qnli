ayisha_age_premise = 3/6
ayisha_age_hypothesis = 1/6

# the hypothesis refers to Ayisha's age in relation to her father's age, also mentioned in the premise
if ayisha_age_hypothesis >= ayisha_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ayisha_age_premise'
    label = "contradiction"
elif ayisha_age_hypothesis == ayisha_age_premise:
    # check if the hypothesis value exactly equals 'ayisha_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Ayisha's age in relation to her father's age
    # any fraction of Ayisha's age less than 'ayisha_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
