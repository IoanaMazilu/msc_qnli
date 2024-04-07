# Premise: City A to city B, Raja drove for 1 hour at 72 mph and for 3 hours at 80 mph.
# Hypothesis: City A to city B, Raja drove for less than 4 hour at 72 mph and for 3 hours at 80 mph.
# Golden Label: entailment

drive_time_speed1_premise = 1
drive_speed1_premise = 72
drive_time_speed2_premise = 3
drive_speed2_premise = 80

drive_time_speed1_hypothesis = 4
drive_speed1_hypothesis = 72
drive_time_speed2_hypothesis = 3
drive_speed2_hypothesis = 80

# the hypothesis refers to the driving time and speed from city A to city B mentioned in the premise
if drive_time_speed1_hypothesis <= drive_time_speed1_premise:
    # check if the duration of 'drive_time_speed1_hypothesis' contradicts the driving time at speed1 in the premise
    label = "contradiction"
elif drive_speed1_hypothesis != drive_speed1_premise:
    # check if the speed1 of driving in the hypothesis contradicts the speed1 of driving reported in the premise
    label = "contradiction"
elif drive_time_speed2_hypothesis != drive_time_speed2_premise:
    # check if the duration of 'drive_time_speed2_hypothesis' contradicts the driving time at speed2 in the premise
    label = "contradiction"
elif drive_speed2_hypothesis != drive_speed2_premise:
    # check if the speed2 of driving in the hypothesis contradicts the speed2 of driving reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

