speed_west_premise = 4
speed_east_premise = 1
speed_west_hypothesis = 7
speed_east_hypothesis = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if speed_west_premise >= speed_west_hypothesis:
    # check if the estimate of'speed_west_hypothesis' contradicts the speed of the first bird in the premise
    label = "contradiction"
elif speed_east_hypothesis!= speed_east_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
