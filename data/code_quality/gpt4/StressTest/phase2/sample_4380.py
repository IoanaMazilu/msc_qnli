# Driving time from City A to City B at 50 mph
drive_time_50mph_premise = 1
drive_time_50mph_hypothesis = 8

# Driving time from City A to City B at 60 mph
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# Checking if the hypothesis contradicts the premise
if drive_time_50mph_hypothesis <= drive_time_50mph_premise:
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    label = "contradiction"
else:
    # The hypothesis provides an overestimate for the drive time at 50 mph, but the exact match for the drive time at 60 mph
    # Thus, the premise does not contradict the hypothesis, but we cannot infer entailment either
    label = "neutral"

print(label)
