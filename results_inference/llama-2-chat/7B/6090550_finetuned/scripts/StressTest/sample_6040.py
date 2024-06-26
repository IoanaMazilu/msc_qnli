start_speed_premise = 10
start_speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20
time_premise = 12
time_hypothesis = 12

# the hypothesis talks about Xavier's speed at a certain time, which is also mentioned in the premise
if start_speed_hypothesis <= start_speed_premise:
    # check if the start speed in the hypothesis contradicts the start speed in the premise
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the increase speed in the hypothesis contradicts the increase speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
