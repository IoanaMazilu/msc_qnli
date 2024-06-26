age_babysitting_start_premise = 78
age_babysitting_start_hypothesis = 18

# the hypothesis refers to the age Jane started baby-sitting, which is also mentioned in the premise
if age_babysitting_start_hypothesis >= age_babysitting_start_premise:
    # check if the hypothesis age contradicts the premise's estimate of less than 'age_babysitting_start_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the age Jane started baby-sitting
    # any age less than 'age_babysitting_start_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
