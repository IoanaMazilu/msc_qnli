speed_west_bird_premise = 4
speed_west_bird_hypothesis = 7
speed_east_bird_premise = 1
speed_east_bird_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if speed_west_bird_premise >= speed_west_bird_hypothesis:
    # check if the estimate of'speed_west_bird_hypothesis' contradicts the speed of the west bird in the premise
    label = "contradiction"
elif speed_east_bird_hypothesis!= speed_east_bird_premise:
    # check if the speed of the east bird in the hypothesis contradicts the speed of the east bird reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
