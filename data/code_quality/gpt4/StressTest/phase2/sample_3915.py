speed_premise = 12
speed_hypothesis = 52

# The hypothesis refers to the constant speed of Lindy running back and forth from Christina to Jack, mentioned in the premise
if speed_hypothesis < speed_premise:
    # Check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_hypothesis > speed_premise:
    # The hypothesis value of speed doesn't contradict the premise, but it cannot be fully entailed from the premise
    label = "neutral"
else:
    # If hypothesis speed is equal to premise speed, the speed in the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
