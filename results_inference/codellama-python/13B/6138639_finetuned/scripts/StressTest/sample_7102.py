first_drive_premise = 340
first_drive_hypothesis = 240
second_drive_premise = 120
second_drive_hypothesis = 120

# the hypothesis talks about the driving distances and speeds, referenced also in the premise
if first_drive_hypothesis >= first_drive_premise:
    # check if the hypothesis value contradicts the estimate of less than 'first_drive_premise'
    label = "contradiction"
elif second_drive_hypothesis!= second_drive_premise:
    # check if the second drive distance in the hypothesis contradicts the second drive distance reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first drive distance
    # any first drive distance less than 'first_drive_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
