total_distance_premise = 1/2
total_distance_hypothesis = 8/2

# the hypothesis talks about the distance Maria traveled, referenced also in the premise
if total_distance_hypothesis <= total_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'total_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)