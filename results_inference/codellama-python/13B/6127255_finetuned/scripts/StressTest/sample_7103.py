miles_first_drive_premise = 240
miles_first_drive_hypothesis = 140
speed_first_drive_premise = 60
speed_first_drive_hypothesis = 60
miles_second_drive_premise = 120
miles_second_drive_hypothesis = 120
speed_second_drive_premise = 40
speed_second_drive_hypothesis = 40

# the hypothesis refers to the miles driven and the speed of driving mentioned in the premise
if miles_first_drive_hypothesis!= miles_first_drive_premise or speed_first_drive_hypothesis!= speed_first_drive_premise:
    # check if the miles driven or the speed of driving in the first drive in the hypothesis contradicts the premise
    label = "contradiction"
elif miles_second_drive_hypothesis!= miles_second_drive_premise or speed_second_drive_hypothesis!= speed_second_drive_premise:
    # check if the miles driven or the speed of driving in the second drive in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
