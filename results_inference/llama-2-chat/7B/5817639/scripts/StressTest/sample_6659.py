average_speed_premise = 60
average_speed_hypothesis = 70
distance_premise = 0
distance_hypothesis = 0

# the hypothesis talks about the average speed of two drivers, referenced also in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of the average speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any average speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# calculate the distance driven by Tom based on the average speed in the hypothesis
distance_hypothesis = (0.5 * (average_speed_hypothesis * 100)) / 60

# check if the distance driven by Tom contradicts the distance driven in the premise
if distance_hypothesis <= distance_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
