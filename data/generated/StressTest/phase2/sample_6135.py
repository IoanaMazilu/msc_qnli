# Premise: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of less than 61 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: entailment

james_hours_worked_premise = 41
james_hours_worked_hypothesis = 61

# The hypothesis talks about the number of hours James worked last week, which is also referenced in the premise
if james_hours_worked_hypothesis <= james_hours_worked_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'james_hours_worked_hypothesis'
    label = "contradiction"
elif james_hours_worked_hypothesis > james_hours_worked_premise:
    # The premise gives a precise number of hours James worked
    # Any number of hours less than 'james_hours_worked_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

