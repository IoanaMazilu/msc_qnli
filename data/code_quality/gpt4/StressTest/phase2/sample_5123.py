lake_speed_premise = 5
lake_speed_hypothesis = 5
river_speed_premise = 4
river_speed_hypothesis = 4

# the hypothesis talks about the speed of the boat on the lake and on the river, both also mentioned in the premise
if lake_speed_hypothesis >= lake_speed_premise:
    # check if the estimate of 'lake_speed_hypothesis' contradicts the speed of the boat on the lake in the premise
    label = "contradiction"
elif river_speed_hypothesis != river_speed_premise:
    # check if the speed of the boat on the river in the hypothesis contradicts the speed of the boat on the river in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
