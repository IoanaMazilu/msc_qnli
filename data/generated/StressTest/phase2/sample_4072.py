# Premise: for Mathura and B starts from Mathura with a speed of less than 75 kmph at 8 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of 25 kmph at 8 p.
# Golden Label: neutral

speed_premise = 75
speed_hypothesis = 25

# the hypothesis states a specific speed for B starting from Mathura, also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # if the speed in the hypothesis is less than the speed in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis speed does not contradict the premise speed, but also is not explicitly mentioned in the premise, we infer neutral
    label = "neutral"

print(label)

