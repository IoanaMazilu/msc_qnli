# Premise: A starts from Delhi with a speed of 25 kmph at 5 a.
# Hypothesis: A starts from Delhi with a speed of 35 kmph at 5 a.
# Golden Label: contradiction

speed_premise = 25
speed_hypothesis = 35

# the hypothesis talks about the speed of A, referenced also in the premise
if speed_premise != speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)

