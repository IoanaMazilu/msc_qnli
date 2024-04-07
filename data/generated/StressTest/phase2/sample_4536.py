# Premise: They both work together for 5 days and then Sushil goes away.
# Hypothesis: They both work together for more than 4 days and then Sushil goes away.
# Golden Label: entailment

work_days_premise = 5
work_days_hypothesis = 4

# the hypothesis refers to the number of days they both work together, which is also mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

