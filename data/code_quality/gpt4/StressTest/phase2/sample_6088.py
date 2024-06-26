work_days_together_premise = 52
work_days_together_hypothesis = 12
remaining_work_days_peter = 10

# the hypothesis talks about the number of days Matt and Peter have worked together and the number of days Peter worked alone, both referenced also in the premise
if work_days_together_hypothesis >= work_days_together_premise:
    # check if the hypothesis' estimate of 'work_days_together_hypothesis' contradicts the premise of less than 'work_days_together_premise'
    label = "contradiction"
elif remaining_work_days_peter != remaining_work_days_peter:
    # check if the number of days Peter worked alone in the hypothesis contradicts the number of days Peter worked alone reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Matt and Peter worked together
    # any number of days less than 'work_days_together_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
