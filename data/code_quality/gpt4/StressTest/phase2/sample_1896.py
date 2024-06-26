work_days_premise = 20
work_days_hypothesis = 10

# the hypothesis refers to the number of days Matt and Peter can do a piece of work together, which is also mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of more than 'work_days_hypothesis'
    label = "contradiction"
elif work_days_premise > work_days_hypothesis:
    # if the number of days in the premise is greater than the 'work_days_hypothesis', we can infer entailment
    label = "entailment"

print(label)
