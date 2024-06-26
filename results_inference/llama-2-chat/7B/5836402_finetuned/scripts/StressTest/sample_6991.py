running_distance_premise = 52
running_distance_hypothesis = 12

# the hypothesis talks about the distance the twins ran, which is also referenced in the premise
if running_distance_hypothesis <= running_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'running_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance run
    # any distance less than 'running_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
