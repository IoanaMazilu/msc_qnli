# Premise: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 31 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: contradiction

james_worked_hours_premise = 41
james_worked_hours_hypothesis = 31

# the hypothesis refers to the number of hours James worked last week, which is mentioned in the premise
if james_worked_hours_hypothesis != james_worked_hours_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours he worked according to the premise
    label = "contradiction"
else:
    # if the hours James worked in the hypothesis do not contradict the hours he worked in the premise, we can infer entailment
    label = "entailment"

print(label)

