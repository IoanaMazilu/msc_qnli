average_speed_premise = 1
average_speed_hypothesis = 4

# the hypothesis refers to a specific ratio of distances between points A, B, and C
if average_speed_premise <= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the information provided in the premise
    label = "contradiction"
else:
    # the premise provides a general information about the ratio of distances, while the hypothesis provides a specific value for the average speed
    # any value of average speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
