drive_hr_premise_1 = 1
drive_hr_premise_2 = 3
drive_hr_hypothesis = 5
drive_speed_premise_1 = 42
drive_speed_premise_2 = 60
drive_speed_hypothesis = 42

# the hypothesis refers to the time Andrew drove and the speed he drove at, mentioned in the premise
if drive_hr_hypothesis <= drive_hr_premise_1 or drive_hr_hypothesis >= drive_hr_premise_2:
    # check if the estimate of 'drive_hr_hypothesis' contradicts the number of hours Andrew drove in the premise
    label = "contradiction"
elif drive_speed_hypothesis!= drive_speed_premise_1 or drive_speed_hypothesis!= drive_speed_premise_2:
    # check if the speed Andrew drove in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
