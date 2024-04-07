# Premise: A starts from Delhi with a speed of 25 kmph at 7 a.
# Hypothesis: A starts from Delhi with a speed of 65 kmph at 7 a.
# Golden Label: contradiction

speed_premise = 25
speed_hypothesis = 65

# the hypothesis refers to the speed of A mentioned in the premise
if speed_premise != speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis equals the premise speed, we can infer entailment
    label = "entailment"

print(label)

