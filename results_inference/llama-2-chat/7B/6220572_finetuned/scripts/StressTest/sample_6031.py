distance_premise = 8/2
distance_hypothesis = 1/2

# the hypothesis talks about the distance traveled before Maria stopped to rest, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled before Maria stopped to rest
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
