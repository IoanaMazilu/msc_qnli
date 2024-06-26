ime_premise = 30
time_premise = 1
time_hypothesis = 1
speed_hypothesis = 60

# the hypothesis talks about the speed of Cara's drive from City A to City B, which is also mentioned in the premise
if speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the speed and time in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
