driving_speed_premise = 12
driving_speed_hypothesis = 32

# the hypothesis talks about the constant driving speed of Cara, also mentioned in the premise
if driving_speed_hypothesis <= driving_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'driving_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving speed
    # any driving speed greater than 'driving_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
