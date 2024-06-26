speed_initial = 90
speed_increase = 20
time_interval = 12

# the hypothesis talks about the initial speed of Xavier, which is also mentioned in the premise
if speed_initial < 90:
    # check if the initial speed in the hypothesis contradicts the initial speed in the premise
    label = "contradiction"
elif speed_increase!= 20:
    # check if the speed increase in the hypothesis contradicts the speed increase in the premise
    label = "contradiction"
else:
    # the premise and hypothesis both mention the time interval
    # but the hypothesis does not provide any additional information about the time interval
    # therefore, the premise and hypothesis are neutral
    label = "neutral"

print(label)
