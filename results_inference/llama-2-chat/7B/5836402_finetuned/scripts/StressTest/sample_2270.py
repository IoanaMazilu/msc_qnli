speed_from_a_to_b_premise = 40
speed_from_b_to_c_premise = 60
speed_from_a_to_b_hypothesis = 80
speed_from_b_to_c_hypothesis = 60

# the hypothesis refers to the speed of Murali's journey from A to B and from B to C, mentioned in the premise
if speed_from_a_to_b_hypothesis!= speed_from_a_to_b_premise:
    # check if the speed of Murali's journey from A to B in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_from_b_to_c_hypothesis!= speed_from_b_to_c_premise:
    # check if the speed of Murali's journey from B to C in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
