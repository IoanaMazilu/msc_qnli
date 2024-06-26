speed_60mph_time_premise = 1
speed_60mph_time_hypothesis = 2
speed_50mph_time_premise = 3
speed_50mph_time_hypothesis = 3

# the hypothesis refers to the driving durations at 60 mph and 50 mph mentioned in the premise
if speed_60mph_time_hypothesis <= speed_60mph_time_premise:
    # check if the hypothesis value contradicts the time duration at 60 mph in the premise
    label = "contradiction"
elif speed_50mph_time_hypothesis != speed_50mph_time_premise:
    # check if the driving duration at 50 mph in the hypothesis contradicts the time duration at 50 mph mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
