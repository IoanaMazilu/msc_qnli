# Premise: Jhon works for 60 days.
# Hypothesis: Jhon works for more than 40 days.
# Golden Label: entailment

work_days_premise = 60
work_days_hypothesis = 40

# the hypothesis refers to the number of days Jhon works mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

