jhon_work_days_premise = 60
jhon_work_days_hypothesis = 40

# the hypothesis talks about the number of days Jhon works, referenced also in the premise
if jhon_work_days_premise <= jhon_work_days_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'jhon_work_days_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Jhon works
    # any number of days greater than 'jhon_work_days_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
