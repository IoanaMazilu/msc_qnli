age_premise = 54
age_hypothesis = 34
years_stopped_babysitting_premise = 10
years_stopped_babysitting_hypothesis = 10

# the hypothesis talks about Jane's age and when she stopped baby-sitting, both referenced in the premise
if age_hypothesis >= age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_premise'
    label = "contradiction"
elif years_stopped_babysitting_hypothesis!= years_stopped_babysitting_premise:
    # check if the number of years stopped baby-sitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
