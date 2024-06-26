years_old_premise = 40
years_old_hypothesis = 20

# the hypothesis talks about the age at which Jane started baby-sitting, referenced also in the premise
if years_old_hypothesis <= years_old_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_old_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age at which Jane started baby-sitting
    # any age less than 'years_old_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
