age_jane_premise = 82
age_jane_hypothesis = 32
years_since_stopped_babysitting_premise = 12
years_since_stopped_babysitting_hypothesis = 12

# the hypothesis talks about Jane's age and the time since she stopped baby-sitting, both also referenced in the premise
if age_jane_hypothesis >= age_jane_premise:
    # check if the hypothesis age contradicts the premise estimate of less than 'age_jane_premise'
    label = "contradiction"
elif years_since_stopped_babysitting_hypothesis!= years_since_stopped_babysitting_premise:
    # check if the time since Jane stopped baby-sitting in the hypothesis contradicts the time since she stopped baby-sitting reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age less than 'age_jane_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
