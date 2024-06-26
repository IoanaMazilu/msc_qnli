driving_time_premise = 1 + 3 = 4
driving_speed_premise = 50
driving_time_hypothesis = 7
driving_speed_hypothesis = 50

# the hypothesis talks about the driving time and speed, also referenced in the premise
if driving_time_hypothesis!= driving_time_premise:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
elif driving_speed_hypothesis!= driving_speed_premise:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
