# Premise: Last week James worked a total of less than 55 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 45 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: neutral

james_work_hours_premise = 55
james_work_hours_hypothesis = 45

# the hypothesis talks about the number of hours James worked last week, referenced also in the premise
if james_work_hours_hypothesis >= james_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of fewer than 'james_work_hours_premise'
    label = "contradiction"
elif james_work_hours_hypothesis < james_work_hours_premise:
    # if the hypothesis value is less than 'james_work_hours_premise' we can infer entailment
    label = "entailment"

print(label)

