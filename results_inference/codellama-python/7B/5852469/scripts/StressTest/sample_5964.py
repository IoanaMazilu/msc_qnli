hours_drive_premise = 4
hours_drive_hypothesis = 8

# the hypothesis refers to the same event as the premise
if hours_drive_hypothesis <= hours_drive_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_drive_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_drive_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
