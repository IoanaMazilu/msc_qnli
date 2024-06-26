west_town_speed_premise = 4
west_town_speed_hypothesis = 3
east_town_speed_premise = 1
east_town_speed_hypothesis = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if west_town_speed_hypothesis <= west_town_speed_premise:
    # check if the estimate of 'west_town_speed_hypothesis' contradicts the speed of the bird in the premise
    label = "contradiction"
elif east_town_speed_hypothesis!= east_town_speed_premise:
    # check if the speed of the bird in the hypothesis contradicts the speed of the bird reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
