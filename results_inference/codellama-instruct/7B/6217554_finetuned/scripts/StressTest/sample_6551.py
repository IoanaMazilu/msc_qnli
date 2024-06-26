bird_speed_west_premise = 4
bird_speed_east_premise = 1
bird_speed_west_hypothesis = 3
bird_speed_east_hypothesis = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if bird_speed_west_hypothesis!= bird_speed_west_premise:
    # check if the speed of the first bird in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif bird_speed_east_hypothesis!= bird_speed_east_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
