speed_from_a_to_b_premise = 30
speed_from_b_to_c_premise = 60
speed_from_a_to_b_hypothesis = 40
speed_from_b_to_c_hypothesis = 60

# the hypothesis refers to the traveling speed from A to B and from B to C mentioned in the premise
if speed_from_a_to_b_hypothesis <= speed_from_a_to_b_premise:
    # check if the hypothesis value contradicts the estimate of more than'speed_from_a_to_b_premise'
    label = "contradiction"
elif speed_from_b_to_c_hypothesis!= speed_from_b_to_c_premise:
    # check if the speed from B to C in the hypothesis contradicts the speed from B to C reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
