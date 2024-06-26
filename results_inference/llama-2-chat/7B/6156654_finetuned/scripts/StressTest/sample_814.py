speed_from_a_to_b_premise = 30
speed_from_b_to_c_premise = 60
speed_from_a_to_b_hypothesis = 40
speed_from_b_to_c_hypothesis = 60

# the hypothesis talks about the speed at which Murali travelled from city A to city B and from city B to city C, which are also mentioned in the premise
if speed_from_a_to_b_hypothesis < speed_from_a_to_b_premise:
    # check if the speed from A to B in the hypothesis contradicts the speed from A to B in the premise
    label = "contradiction"
elif speed_from_b_to_c_hypothesis!= speed_from_b_to_c_premise:
    # check if the speed from B to C in the hypothesis contradicts the speed from B to C in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise speeds, we can infer entailment
    label = "entailment"

print(label)
