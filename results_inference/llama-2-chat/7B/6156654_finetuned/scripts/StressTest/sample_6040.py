speed_start = 10
speed_increase = 20
time_increase = 12
speed_end = 90

# the hypothesis refers to the same situation as the premise, but with different initial speed
if speed_start!= speed_end:
    # check if the initial speed in the hypothesis contradicts the initial speed in the premise
    label = "contradiction"
elif time_increase!= speed_increase:
    # check if the time for increasing speed in the hypothesis contradicts the time for increasing speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
