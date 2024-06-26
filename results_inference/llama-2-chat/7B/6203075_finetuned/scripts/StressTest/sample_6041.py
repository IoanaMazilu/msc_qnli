speed_start = 90
speed_increase = 20
time_interval = 12

# the hypothesis talks about the speed at which Xavier starts and the speed increase every 12 minutes
if speed_start <= speed_increase:
    # check if the speed at which Xavier starts contradicts the hypothesis
    label = "contradiction"
elif time_interval!= 12:
    # check if the time interval in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
