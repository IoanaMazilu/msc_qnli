a_speed_premise = 50
b_speed_premise = 60
c_speed_hypothesis = 40

# the hypothesis refers to the speed at which Murali travelled between cities A and B, and between cities B and C
if c_speed_hypothesis <= b_speed_premise:
    # check if the estimate of 'c_speed_hypothesis' contradicts the speed at which Murali travelled between cities A and B in the premise
    label = "contradiction"
elif c_speed_hypothesis!= b_speed_premise:
    # check if the speed at which Murali travelled between cities B and C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
