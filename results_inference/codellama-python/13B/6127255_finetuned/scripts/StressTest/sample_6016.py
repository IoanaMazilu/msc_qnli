jane_age_start_babysitting_premise = 40
jane_age_start_babysitting_hypothesis = 20

# the hypothesis talks about the age Jane started babysitting, referenced also in the premise
if jane_age_start_babysitting_hypothesis >= jane_age_start_babysitting_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jane_age_start_babysitting_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age Jane started babysitting
    # any age less than 'jane_age_start_babysitting_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
