ayisha_age_premise = 1/6
ayisha_age_hypothesis = 1/6

# the hypothesis refers to Ayisha's age as mentioned in the premise
if ayisha_age_hypothesis >= ayisha_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ayisha_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Ayisha's age
    # any age less than 'ayisha_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
