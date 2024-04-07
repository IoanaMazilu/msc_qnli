# Premise: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of more than 21 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: entailment

james_hours_worked_premise = 41
james_hours_worked_hypothesis = 21

# the hypothesis refers to the number of hours James worked last week, mentioned also in the premise
if james_hours_worked_premise <= james_hours_worked_hypothesis:
    # check if the estimate of 'james_hours_worked_hypothesis' contradicts the number of hours James worked in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
