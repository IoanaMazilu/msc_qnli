# Premise: On her way back, Venki drives more than 25 miles per hour and stops in Town Y which is midway between Town X and Town Z.
# Hypothesis: On her way back, Venki drives 45 miles per hour and stops in Town Y which is midway between Town X and Town Z.
# Golden Label: neutral

driving_speed_premise = 25
driving_speed_hypothesis = 45

# the hypothesis talks about Venki's driving speed and the midway stop in town Y, both mentioned also in the premise
if driving_speed_hypothesis <= driving_speed_premise:
    # check if the hypothesis speed contradicts the premise estimate of more than 'driving_speed_premise' mph
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving speed
    # any speed greater than 'driving_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

