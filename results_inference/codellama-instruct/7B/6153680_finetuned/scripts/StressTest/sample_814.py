speed_A_B_premise = 30
speed_B_C_premise = 60
speed_A_B_hypothesis = 40
speed_B_C_hypothesis = 60

# the hypothesis refers to the speed of Murali's travel from city A to B and from B to C, as mentioned in the premise
if speed_A_B_hypothesis <= speed_A_B_premise:
    # check if the speed of Murali's travel from A to B in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_B_C_hypothesis!= speed_B_C_premise:
    # check if the speed of Murali's travel from B to C in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
