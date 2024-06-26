# Defining variables
drive_time_premise_1 = 1
drive_time_premise_2 = 3
drive_time_hypothesis_1 = 1
drive_time_hypothesis_2 = 3
drive_speed_premise_1 = 42
drive_speed_premise_2 = 60
drive_speed_hypothesis_1 = 42
drive_speed_hypothesis_2 = 60

# Calculating drive time for premise
drive_time_premise_1_hrs = drive_time_premise_1 / 60
drive_time_premise_2_hrs = drive_time_premise_2 / 60

# Calculating drive time for hypothesis
drive_time_hypothesis_1_hrs = drive_time_hypothesis_1 / 60
drive_time_hypothesis_2_hrs = drive_time_hypothesis_2 / 60

# Checking if the drive times in the hypothesis contradict the drive times in the premise
if drive_time_hypothesis_1_hrs!= drive_time_premise_1_hrs or drive_time_hypothesis_2_hrs!= drive_time_premise_2_hrs:
    label = "contradiction"
else:
    # Checking if the drive speeds in the hypothesis contradict the drive speeds in the premise
    if drive_speed_hypothesis_1!= drive_speed_premise_1 or drive_speed_hypothesis_2!= drive_speed_premise_2:
        label = "contradiction"
    else:
        # If the drive times and speeds in the hypothesis do not contradict the ones in the premise, we can infer entailment
        label = "entailment"

print(label)
