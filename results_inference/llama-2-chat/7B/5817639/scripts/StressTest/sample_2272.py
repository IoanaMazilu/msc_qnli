average_speed_premise = 0
average_speed_hypothesis = 0

# the premise gives a ratio of distances, which we use to calculate the average speed
if average_speed_premise <= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed, which can be entailed from the ratio of distances
    label = "entailment"

print(label)
