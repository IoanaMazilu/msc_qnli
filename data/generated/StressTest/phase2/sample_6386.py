# Premise: Last week James worked a total of 45 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 35 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: contradiction

hours_worked_james_premise = 45
hours_worked_james_hypothesis = 35

# the hypothesis refers to the number of hours that James worked, also mentioned in the premise
if hours_worked_james_hypothesis != hours_worked_james_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis and premise are in agreement, we can infer entailment
    label = "entailment"
    
print(label)

