premise_speed_AB = 40
premise_speed_BC = 60
hypothesis_speed_AB = 80
hypothesis_speed_BC = 60

# the hypothesis refers to the speed of travel from city A to city B and from city B to city C
if hypothesis_speed_AB > premise_speed_AB:
    # check if the estimate of 'hypothesis_speed_AB' contradicts the speed of travel from city A to city B in the premise
    label = "contradiction"
elif hypothesis_speed_BC!= premise_speed_BC:
    # check if the speed of travel from city B to city C in the hypothesis contradicts the speed of travel from city B to city C in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
