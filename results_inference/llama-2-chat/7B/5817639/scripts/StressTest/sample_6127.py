people_premise = 41
people_hypothesis = 31

# the hypothesis talks about the number of people who have visited neither Iceland nor Norway
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited neither Iceland nor Norway
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
