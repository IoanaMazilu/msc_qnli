miles_first_drive_premise = 300
miles_first_drive_hypothesis = 600
miles_second_drive_premise = 120
miles_second_drive_hypothesis = 120

# the hypothesis talks about the distance Joe drives at two different speeds, which is also referred to in the premise
if miles_first_drive_hypothesis <= miles_first_drive_premise or miles_second_drive_hypothesis != miles_second_drive_premise:
    # check if the number of miles driven at 60mph or 40mph in the hypothesis contradicts the number of miles driven at the same speeds in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of miles driven at 60mph
    # any number of miles greater than 'miles_first_drive_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
