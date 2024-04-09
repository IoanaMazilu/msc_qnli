distance_premise = 31
distance_hypothesis = 61

# the hypothesis talks about the distance traveled by Bob, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Bob
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
