average_speed_premise = 4
average_speed_hypothesis = 1

# the hypothesis talks about the ratio of distances between A to B and B to C
if average_speed_premise <= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio greater than 'average_speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
