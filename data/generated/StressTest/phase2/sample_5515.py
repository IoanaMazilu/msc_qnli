# Premise: A starts from Delhi with a speed of less than 45 kmph at 5 a.
# Hypothesis: A starts from Delhi with a speed of 25 kmph at 5 a.
# Golden Label: neutral

speed_premise = 45
speed_hypothesis = 25

# the hypothesis talks about the speed of A when starting from Delhi, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the premise of less than 'speed_premise'
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # the premise provides an upper limit for the speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

