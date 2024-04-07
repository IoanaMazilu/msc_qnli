# Premise: for Mathura and B starts from Mathura with a speed of 25 kmph at 8 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of 85 kmph at 8 p.
# Golden Label: contradiction

speed_B_premise = 25
speed_B_hypothesis = 85

# the hypothesis refers to the speed of B mentioned in the premise
if speed_B_premise != speed_B_hypothesis:
    # check if the speed of B in the hypothesis contradicts the speed of B in the premise
    label = "contradiction"
else:
    # if the speed of B in the hypothesis is the same as the speed of B in the premise, we can infer entailment
    label = "entailment"

print(label)

