speed_premise = 90
speed_increase_premise = 20
time_interval_premise = 12

speed_hypothesis = 90
speed_increase_hypothesis = 20
time_interval_hypothesis = 12

# hypothesis talks about Xavier's starting speed and speed increase which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise of 'speed_premise'
    label = "contradiction"
elif speed_increase_hypothesis != speed_increase_premise or time_interval_hypothesis != time_interval_premise:
    # check if the speed increase or time interval in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
