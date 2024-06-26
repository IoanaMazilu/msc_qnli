speed_start_premise = 90
speed_increase_premise = 20
speed_start_hypothesis = 90
speed_increase_hypothesis = 20
time_interval = 12

# the hypothesis talks about the speed and the speed increase of Xavier, which are also mentioned in the premise
if speed_start_hypothesis <= speed_start_premise:
    # check if the hypothesis value contradicts the premise value of the starting speed
    label = "contradiction"
elif speed_increase_hypothesis!= speed_increase_premise:
    # check if the hypothesis value contradicts the premise value of the speed increase
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
