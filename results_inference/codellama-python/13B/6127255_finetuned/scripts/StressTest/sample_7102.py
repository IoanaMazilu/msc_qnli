first_drive_distance_premise = 340
first_drive_distance_hypothesis = 240
second_drive_distance_premise = 120
second_drive_distance_hypothesis = 120

# the hypothesis refers to the distances driven at 60mph and 40mph, which are also mentioned in the premise
if first_drive_distance_hypothesis > first_drive_distance_premise:
    # check if the distance driven at 60mph in the hypothesis contradicts the distance driven at 60mph in the premise
    label = "contradiction"
elif second_drive_distance_hypothesis!= second_drive_distance_premise:
    # check if the distance driven at 40mph in the hypothesis contradicts the distance driven at 40mph in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first drive distance
    # any distance less than 'first_drive_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
