# Premise: for Mathura and B starts from Mathura with a speed of 25 kmph at 8 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of less than 75 kmph at 8 p.
# Golden Label: entailment

speed_B_premise = 25
speed_B_hypothesis = 75

# the hypothesis refers to the speed of B mentioned in the premise
if speed_B_premise >= speed_B_hypothesis:
    # check if the estimate of 'speed_B_hypothesis' contradicts the speed of B in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

