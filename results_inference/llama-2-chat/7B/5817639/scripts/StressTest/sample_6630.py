speed_premise = 15  # from premise
speed_hypothesis = 15  # from hypothesis
distance_premise = 500  # from premise
distance_hypothesis = 800  # from hypothesis

# the hypothesis talks about the time it takes to cover a distance, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
