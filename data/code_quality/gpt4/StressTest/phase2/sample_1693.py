age_start_babysitting_premise = 86
age_start_babysitting_hypothesis = 16

# the hypothesis states an exact age when Jane started baby-sitting, while the premise provides an upper limit
if age_start_babysitting_hypothesis >= age_start_babysitting_premise:
    # check if the hypothesis age contradicts the premise's upper limit
    label = "contradiction"
else:
    # the premise gives only an upper limit for the age when Jane started baby-sitting
    # any age less than 'age_start_babysitting_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
