# Premise: A starts from Delhi with a speed of 20 kmph at 7 a.
# Hypothesis: A starts from Delhi with a speed of less than 20 kmph at 7 a.
# Golden Label: contradiction

speed_premise = 20
speed_hypothesis = 20

# the hypothesis refers to the speed of A mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the speed mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

