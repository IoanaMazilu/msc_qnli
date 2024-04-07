# Premise: for Mathura and B starts from Mathura with a speed of 30 kmph at 9 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of less than 30 kmph at 9 p.
# Golden Label: contradiction

speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the starting speed of B mentioned in the premise
if speed_hypothesis < speed_premise:
    # check if the hypothesis speed contradicts the speed in the premise
    label = "contradiction"
elif speed_hypothesis > speed_premise:
    # check if the hypothesis speed is greater than the premise speed
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)

