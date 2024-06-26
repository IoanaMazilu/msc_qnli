years_premise = 20
years_hypothesis = 40

# the hypothesis talks about the age at which Jane started baby-sitting, referenced also in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age at which Jane started baby-sitting
    # any age less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
