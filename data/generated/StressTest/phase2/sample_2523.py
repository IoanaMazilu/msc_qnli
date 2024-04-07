# Premise: for Mathura and B starts from Mathura with a speed of 30 kmph at 9 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of more than 20 kmph at 9 p.
# Golden Label: entailment

speed_B_premise = 30
speed_B_hypothesis = 20

# the hypothesis refers to the speed of B from the premise
if speed_B_premise < speed_B_hypothesis:
    # check if the speed of B in the premise contradicts the estimate of 'speed_B_hypothesis'
    label = "contradiction"
elif speed_B_premise > speed_B_hypothesis:
    # check if the speed of B in the hypothesis contradicts the speed of B reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

