# Premise: A starts from Delhi with a speed of 25 kmph at 5 a.
# Hypothesis: A starts from Delhi with a speed of less than 45 kmph at 5 a.
# Golden Label: entailment

speed_premise = 25
speed_hypothesis = 45

# the hypothesis refers to the speed of A mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of 'speed_hypothesis' contradicts the speed of A in the premise
    label = "contradiction"
else:
    # the premise gives exact speed for A
    # any speed less than 'speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

