# Premise: for Mathura and B starts from Mathura with a speed of more than 10 kmph at 6 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of 40 kmph at 6 p.
# Golden Label: neutral

speed_b_premise = 10
speed_b_hypothesis = 40

# the hypothesis talks about B's speed, referenced also in the premise
if speed_b_hypothesis <= speed_b_premise:
    # check if the hypothesis speed contradicts the premise estimate of more than 'speed_b_premise' kmph
    label = "contradiction"
else:
    # the premise gives only an estimate for B's speed
    # any speed greater than 'speed_b_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

