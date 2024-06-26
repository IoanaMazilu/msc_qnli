yolanda_speed_premise = 3
bob_speed_premise = 4
yolanda_speed_hypothesis = 5
bob_speed_hypothesis = 4

# the hypothesis refers to Yolanda's walking rate and Bob's walking rate mentioned in the premise
if yolanda_speed_premise <= yolanda_speed_hypothesis and bob_speed_premise == bob_speed_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif bob_speed_hypothesis!= bob_speed_premise:
    # check if the speed of Bob in the hypothesis contradicts the speed of Bob in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
