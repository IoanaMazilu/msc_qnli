# Premise: On her way back, Swetha drives 30 miles per hour and stops in Town Y which is midway between Town A and Town C.
# Hypothesis: On her way back, Swetha drives less than 80 miles per hour and stops in Town Y which is midway between Town A and Town C.
# Golden Label: entailment

speed_premise = 30
speed_hypothesis = 80

# the hypothesis mentions the speed at which Swetha drives which is also specified in the premise
if speed_hypothesis < speed_premise:
    # check if the speed hypothesized contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_hypothesis == speed_premise:
    # if the speed in the hypothesis is the same as the one in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only a certain speed
    # any speed less than 'speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

