# Premise: Last week James worked a total of less than 62 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Hypothesis: Last week James worked a total of 42 hours If Harry and James were paid the same amount last week, how many hours did Harry work last week?
# Golden Label: neutral

hours_worked_james_premise = 62
hours_worked_james_hypothesis = 42

# The hypothesis refers to the hours James worked last week, which is also mentioned in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # Check if the hours James worked last week in the hypothesis contradicts the estimate of less than 'hours_worked_james_premise'
    label = "contradiction"
elif hours_worked_james_hypothesis < hours_worked_james_premise:
    # If the hours James worked last week in the hypothesis is less than 'hours_worked_james_premise', it is consistent with the premise
    # However, it cannot be explicitly entailed from the premise as the premise only provides an estimate
    label = "neutral"

print(label)

