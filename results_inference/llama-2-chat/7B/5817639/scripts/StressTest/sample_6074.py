miles_traveled_premise = 8
miles_traveled_hypothesis = 5
speed_premise = 40
speed_hypothesis = 60
stopped_time_premise = 15
stopped_time_hypothesis = 15

# the hypothesis talks about the distance and speed traveled by Jerry, referenced also in the premise
if miles_traveled_hypothesis <= miles_traveled_premise:
    # check if the hypothesis value contradicts the estimate of the distance traveled in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the estimated speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
