#drive_time_premise = 2
#drive_time_hypothesis = 1
#drive_speed_premise = 44
#drive_speed_hypothesis = 44
#drive_time_at_speed_premise = 3
#drive_time_at_speed_hypothesis = 3

# the hypothesis talks about the driving time and speed from city A to city B, which is also mentioned in the premise
# first, we check the driving time at 44 mph
if drive_time_hypothesis >= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
elif drive_speed_hypothesis!= drive_speed_premise:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
elif drive_time_at_speed_hypothesis!= drive_time_at_speed_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time at 44 mph
    # any driving time less than 'drive_time_premise' at 44 mph is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
