speed_west_premise = 4
speed_west_hypothesis = 3
speed_east_premise = 1
speed_east_hypothesis = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if speed_west_hypothesis!= speed_west_premise:
    # check if the speed of the west bird in the hypothesis contradicts the speed of the west bird reported in the premise
    label = "contradiction"
elif speed_east_hypothesis!= speed_east_premise:
    # check if the speed of the east bird in the hypothesis contradicts the speed of the east bird reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
