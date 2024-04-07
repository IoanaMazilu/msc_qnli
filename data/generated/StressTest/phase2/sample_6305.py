# Premise: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 61 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: contradiction

james_work_hours_premise = 41
james_work_hours_hypothesis = 61

# the hypothesis refers to the number of hours James worked which is also mentioned in the premise
if james_work_hours_hypothesis != james_work_hours_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours he worked in the premise
    label = "contradiction"
else:
    # if the hypothesis and premise values for the number of hours James worked are the same, we can infer entailment
    label = "entailment"

print(label)

