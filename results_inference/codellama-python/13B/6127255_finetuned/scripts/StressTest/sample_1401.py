work_days_premise = 75
work_days_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar can do the work alone, mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
