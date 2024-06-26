hours_premise = 35
hours_hypothesis = 75

# the hypothesis refers to the number of hours worked each week, which is also mentioned in the premise
if hours_hypothesis <= hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific number of hours worked each week, and any number of hours lower than 'hours_hypothesis' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
