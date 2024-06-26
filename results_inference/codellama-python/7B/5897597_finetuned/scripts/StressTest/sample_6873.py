work_days_premise = 60
work_days_hypothesis = 40

# the hypothesis refers to the number of days Jhon works, mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the number of work days in the premise contradicts the estimate of more than 'work_days_hypothesis'
    label = "contradiction"
else:
    # if the number of work days in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
