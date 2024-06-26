distance_walked_premise = 80
distance_walked_hypothesis = 20

# the hypothesis talks about the distance Rasik walked towards north, referenced also in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_walked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance walked
    # any distance less than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
