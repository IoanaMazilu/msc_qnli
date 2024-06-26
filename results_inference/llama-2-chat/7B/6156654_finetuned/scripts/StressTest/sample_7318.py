jim_stretch_time_premise = 78
jim_stretch_time_hypothesis = 18
car_running_time_premise = 78
car_running_time_hypothesis = 18

# the hypothesis talks about the time Jim takes to stretch and Cara's running time, both mentioned in the premise
if jim_stretch_time_hypothesis >= car_running_time_premise:
    # check if the hypothesis time for Jim's stretch contradicts the premise time for Cara's running
    label = "contradiction"
else:
    # if the hypothesis time for Jim's stretch is less than Cara's running time, it does not contradict the premise
    label = "neutral"

print(label)
