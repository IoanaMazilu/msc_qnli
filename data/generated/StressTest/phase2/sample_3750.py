# Premise: They both work together for 5 days and then Sushil goes away.
# Hypothesis: They both work together for more than 1 days and then Sushil goes away.
# Golden Label: entailment

work_days_premise = 5
work_days_hypothesis = 1

# the hypothesis refers to the number of days they both work together as mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the hypothesis estimate contradicts the number of days they worked together in the premise
    label = "contradiction"
else:
    # if the estimate of 'work_days_hypothesis' does not contradict the number of days in the premise, we can infer entailment
    label = "entailment"

print(label)

