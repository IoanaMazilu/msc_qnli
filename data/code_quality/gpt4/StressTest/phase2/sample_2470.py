drive_time_50mph_premise = 4
drive_time_50mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the drive time at 50 mph and 60 mph from city A to city B mentioned in the premise
if drive_time_50mph_hypothesis >= drive_time_50mph_premise:
    # check if the 'drive_time_50mph_hypothesis' contradicts the premise of less than 'drive_time_50mph_premise'
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the 'drive_time_60mph_hypothesis' contradicts the 'drive_time_60mph_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
