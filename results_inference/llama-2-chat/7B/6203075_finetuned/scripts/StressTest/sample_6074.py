miles_traveled_premise = 8
speed_premise = 40
time_stopped_premise = 15
miles_traveled_hypothesis = 5
speed_hypothesis = 40
time_stopped_hypothesis = 15
time_traveled_hypothesis = 20
speed_traveled_hypothesis = 60

# the hypothesis talks about the distance traveled, average speed, and time stopped, all of which are also mentioned in the premise
if miles_traveled_hypothesis!= miles_traveled_premise or speed_hypothesis!= speed_premise or time_stopped_hypothesis!= time_stopped_premise:
    # check if the distance traveled, average speed or time stopped in the hypothesis contradicts the ones in the premise
    label = "contradiction"
elif miles_traveled_hypothesis!= miles_traveled_premise:
    # check if the distance traveled in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
