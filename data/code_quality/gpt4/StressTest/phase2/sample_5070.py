initial_speed_premise = 90
initial_speed_hypothesis = 40
speed_increase_interval = 12
speed_increase_rate = 10

# the hypothesis refers to the initial speed and speed increase pattern of Xavier which is also mentioned in the premise
if initial_speed_premise <= initial_speed_hypothesis:
    # check if the initial speed in the hypothesis contradicts the initial speed in the premise
    label = "contradiction"
elif speed_increase_interval != 12 or speed_increase_rate != 10:
    # check if the speed increase pattern in the hypothesis contradicts the pattern in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
