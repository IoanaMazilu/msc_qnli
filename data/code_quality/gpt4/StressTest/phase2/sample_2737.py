beat_distance_premise = 504
beat_distance_hypothesis = 104

# the hypothesis talks about the distance by which Mohan beats Rohan, which is also mentioned in the premise
if beat_distance_hypothesis >= beat_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'beat_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance by which Mohan beats Rohan
    # any distance less than 'beat_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
