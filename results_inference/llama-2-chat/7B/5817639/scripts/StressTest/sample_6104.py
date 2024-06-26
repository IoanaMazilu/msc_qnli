jane_age_premise = 18
jane_age_hypothesis = 58

# the hypothesis talks about the age at which Jane started baby-sitting, referenced also in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of 'jane_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age at which she started baby-sitting
    # any age greater than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
