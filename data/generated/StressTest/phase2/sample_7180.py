# Premise: City A to city B, Andrew drove for less than 5 hr at 42 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 1 hr at 42 mph and for 3 hours at 60 mph.
# Golden Label: neutral

drive_time_premise = 5
drive_time_hypothesis = 1
drive_speed_premise = 42
drive_speed_hypothesis = 42
drive_time2_premise = 3
drive_time2_hypothesis = 3
drive_speed2_premise = 60
drive_speed2_hypothesis = 60

# The hypothesis talks about the driving time and speed from city A to city B, also mentioned in the premise
if drive_time_hypothesis >= drive_time_premise:
    # Check if the proposed driving time in the hypothesis contradicts the estimate of less than 'drive_time_premise' hours
    label = "contradiction"
elif drive_speed_hypothesis != drive_speed_premise:
    # Check if the driving speed in the hypothesis contradicts the driving speed mentioned in the premise
    label = "contradiction"
elif drive_time2_hypothesis != drive_time2_premise:
    # Check if the second driving time in the hypothesis contradicts the second driving time mentioned in the premise
    label = "contradiction"
elif drive_speed2_hypothesis != drive_speed2_premise:
    # Check if the second driving speed in the hypothesis contradicts the second driving speed mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

