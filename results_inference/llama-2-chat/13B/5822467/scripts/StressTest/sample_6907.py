# define variables for the numerical entities in the premise and hypothesis
drive_time_premise = 2 * 60  # 2 hours x 60 minutes/hour = 120 minutes
drive_time_hypothesis = 3 * 60  # 3 hours x 60 minutes/hour = 180 minutes
speed_premise = 44  # premise mentions 44 mph
speed_hypothesis = 60  # hypothesis mentions 60 mph

# compare the drive time in the premise and hypothesis
if drive_time_premise <= drive_time_hypothesis:
    # check if the estimate of 'drive_time_hypothesis' contradicts the drive time in the premise
    label = "contradiction"
elif drive_time_hypothesis!= drive_time_premise:
    # check if the drive time in the hypothesis contradicts the drive time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

# compare the speed in the premise and hypothesis
if speed_premise <= speed_hypothesis:
    # check if the estimate of'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time and speed
    # any drive time and speed greater than the premise's estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
