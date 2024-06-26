start_speed_premise = 10
start_speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20

# the hypothesis refers to the starting speed and increase speed mentioned in the premise
if start_speed_hypothesis <= start_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'start_speed_premise'
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the increase speed in the hypothesis contradicts the increase speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
