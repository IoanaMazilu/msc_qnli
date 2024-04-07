# Premise: Last week James worked a total of less than 51 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: neutral

hours_worked_james_premise = 51
hours_worked_james_hypothesis = 41

# the hypothesis talks about the number of hours James worked last week, also mentioned in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_worked_james_premise' hours
    label = "contradiction"
elif hours_worked_james_hypothesis < hours_worked_james_premise:
    # The premise gives the upper limit for the number of hours James worked
    # Any number of hours less than 'hours_worked_james_premise' is consistent with the premise, thus may infer entailment
    label = "entailment"

print(label)
