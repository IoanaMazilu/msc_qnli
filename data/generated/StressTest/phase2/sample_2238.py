# Premise: He worked for 9 days before she was joined by Sandra.
# Hypothesis: He worked for more than 8 days before she was joined by Sandra.
# Golden Label: entailment

work_days_premise = 9
work_days_hypothesis = 8

# the hypothesis refers to the number of work days mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

