west_town_speed_premise = 7
west_town_speed_hypothesis = 4
east_town_speed_premise = 1
east_town_speed_hypothesis = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if west_town_speed_hypothesis <= west_town_speed_premise:
    # check if the estimate of 'west_town_speed_hypothesis' contradicts the speed of the bird leaving from West-Town in the premise
    label = "contradiction"
elif east_town_speed_hypothesis!= east_town_speed_premise:
    # check if the speed of the bird leaving from East-Town in the hypothesis contradicts the speed of the bird leaving from East-Town in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
