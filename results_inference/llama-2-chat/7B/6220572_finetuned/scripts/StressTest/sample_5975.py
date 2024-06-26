miles_traveled_premise = 8
miles_traveled_hypothesis = 6
speed_miles_hour_premise = 40
speed_miles_hour_hypothesis = 40
stopped_minutes_premise = 11
stopped_minutes_hypothesis = 11
total_miles_traveled_premise = 20
total_miles_traveled_hypothesis = 20

# the hypothesis talks about the number of miles traveled, speed, and stopped time, referenced also in the premise
if miles_traveled_hypothesis!= miles_traveled_premise:
    # check if the number of miles traveled in the hypothesis contradicts the number of miles traveled reported in the premise
    label = "contradiction"
elif speed_miles_hour_hypothesis!= speed_miles_hour_premise:
    # check if the speed of travel in the hypothesis contradicts the speed of travel reported in the premise
    label = "contradiction"
elif stopped_minutes_hypothesis!= stopped_minutes_premise:
    # check if the number of stopped minutes in the hypothesis contradicts the number of stopped minutes reported in the premise
    label = "contradiction"
elif total_miles_traveled_hypothesis!= total_miles_traveled_premise:
    # check if the total number of miles traveled in the hypothesis contradicts the total number of miles traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
