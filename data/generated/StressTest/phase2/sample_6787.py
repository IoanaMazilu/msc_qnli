# Premise: Last week James worked a total of more than 21 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 41 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: neutral

work_hours_james_premise = 21
work_hours_james_hypothesis = 41

# the hypothesis talks about the number of hours James worked last week, mentioned also in the premise
if work_hours_james_hypothesis <= work_hours_james_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_james_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James worked
    # any number of hours greater than 'work_hours_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

