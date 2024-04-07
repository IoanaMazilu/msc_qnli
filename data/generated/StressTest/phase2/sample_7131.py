# Premise: Patanjali walked for 3 days.
# Hypothesis: Patanjali walked for more than 2 days.
# Golden Label: entailment

walk_days_premise = 3
walk_days_hypothesis = 2

# the hypothesis refers to the number of days Patanjali walked, which is also mentioned in the premise
if walk_days_premise <= walk_days_hypothesis:
    # check if the hypothesis estimate contradicts the number of days walked in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

