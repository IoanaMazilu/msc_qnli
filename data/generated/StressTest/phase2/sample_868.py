# Premise: A starts from Delhi with a speed of less than 70 kmph at 7 a.
# Hypothesis: A starts from Delhi with a speed of 20 kmph at 7 a.
# Golden Label: neutral

speed_premise = 70
speed_hypothesis = 20

# the hypothesis talks about the speed of A, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis speed contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of A
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

