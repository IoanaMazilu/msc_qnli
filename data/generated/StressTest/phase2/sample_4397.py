# Premise: Last week James worked a total of 42 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of less than 42 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: contradiction

james_work_hours_premise = 42
james_work_hours_hypothesis = 42

# the hypothesis refers to the number of hours James worked in the same week
if james_work_hours_hypothesis >= james_work_hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

