distance_sisters_premise = 52
distance_sisters_hypothesis = 12

# the hypothesis talks about the distance each sister ran, which is also mentioned in the premise
if distance_sisters_hypothesis >= distance_sisters_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_sisters_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance, which is less than 52 km
    # any distance less than 52 km is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
