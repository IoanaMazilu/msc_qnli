jane_age_premise = 40
jane_age_hypothesis = 20

# the hypothesis talks about Jane's age when she started babysitting, which is also referenced in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'jane_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age less than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
