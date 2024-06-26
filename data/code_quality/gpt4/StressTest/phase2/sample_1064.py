old_mercedes_speed_premise = 4
old_mercedes_speed_hypothesis = 8

# the hypothesis refers to the speed of an object compared to Mohan's old Mercedes, which is also referenced in the premise
if old_mercedes_speed_hypothesis == old_mercedes_speed_premise:
    # check if the speed ratio in the hypothesis matches the speed ratio in the premise
    label = "entailment"
elif old_mercedes_speed_hypothesis < old_mercedes_speed_premise:
    # check if the speed ratio in the hypothesis contradicts the speed ratio in the premise
    label = "contradiction"
else:
    # if the speed ratio in the hypothesis is greater than the speed ratio in the premise, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
