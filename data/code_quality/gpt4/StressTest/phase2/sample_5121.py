lake_speed_premise = 5
lake_speed_hypothesis = 8
river_speed_premise = 4
river_speed_hypothesis = 4

# the hypothesis refers to the speeds of the boat on the lake and the river, which are also mentioned in the premise
if lake_speed_premise > lake_speed_hypothesis:
    # check if the estimate of 'lake_speed_hypothesis' contradicts the speed of the boat on the lake in the premise
    label = "contradiction"
elif river_speed_premise != river_speed_hypothesis:
    # check if the speed of the boat on the river in the hypothesis contradicts the speed of the boat on the river reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
