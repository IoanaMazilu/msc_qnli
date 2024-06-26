ayisha_age_premise = 1/6
ayisha_age_hypothesis = 3/6

# the hypothesis talks about the proportion of Ayisha's age to her father's age, also referenced in the premise
if ayisha_age_hypothesis <= ayisha_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ayisha_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the proportion of Ayisha's age
    # any proportion less than 'ayisha_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
