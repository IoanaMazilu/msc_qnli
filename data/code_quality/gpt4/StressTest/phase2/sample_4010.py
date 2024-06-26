running_speed_premise = 10
running_speed_hypothesis = 50

# The hypothesis refers to the constant running speed of Lindy mentioned in the premise
if running_speed_premise != running_speed_hypothesis:
    # Check if the speed of Lindy in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # If the speed of Lindy in the hypothesis does not contradict the speed mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
