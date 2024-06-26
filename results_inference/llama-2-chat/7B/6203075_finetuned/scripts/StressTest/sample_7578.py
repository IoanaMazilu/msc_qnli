work_days_premise = 8
work_days_hypothesis = 7

# the hypothesis talks about the number of days they took to complete the work, which is also referenced in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of more than 'work_days_hypothesis'
    label = "contradiction"
else:
    # if the number of days in the premise is greater than 'work_days_hypothesis', we can infer entailment
    label = "entailment"

print(label)
