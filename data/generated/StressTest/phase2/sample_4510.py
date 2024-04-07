# Premise: Last week James worked a total of more than 11 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: neutral

hours_worked_james_premise = 11
hours_worked_james_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week as mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the premise's estimate of more than 'hours_worked_james_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James worked 
    # any number of hours greater than 'hours_worked_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

