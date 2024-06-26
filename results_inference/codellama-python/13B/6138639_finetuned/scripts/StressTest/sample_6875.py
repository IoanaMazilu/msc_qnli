jhon_work_days_premise = 60
jhon_work_days_hypothesis = 60

# the hypothesis talks about the number of days Jhon works, referenced also in the premise
if jhon_work_days_hypothesis >= jhon_work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jhon_work_days_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of days Jhon works
    # any number of days less than 'jhon_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
