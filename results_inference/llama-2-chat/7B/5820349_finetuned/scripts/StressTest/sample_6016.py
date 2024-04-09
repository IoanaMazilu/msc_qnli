babysitting_age_premise = 40
babysitting_age_hypothesis = 20

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_hypothesis >= babysitting_age_premise:
    # check if the hypothesis age contradicts the premise of being less than 'babysitting_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age Jane started babysitting
    # any age less than 'babysitting_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
