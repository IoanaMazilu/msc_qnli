# Premise: Last week James worked a total of 42 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of less than 62 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: entailment

hours_worked_james_premise = 42
hours_worked_james_hypothesis = 62

# the hypothesis refers to the number of hours James worked last week mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the estimate of 'hours_worked_james_hypothesis' contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

