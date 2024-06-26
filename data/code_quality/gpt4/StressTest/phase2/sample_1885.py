distance_premise = 55
distance_hypothesis = 45

# the hypothesis talks about the distance between w and y, referenced also in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance between w and y
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
