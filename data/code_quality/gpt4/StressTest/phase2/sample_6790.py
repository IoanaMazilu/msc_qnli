distance_premise = 10
distance_hypothesis = 50

# the hypothesis and premise make reference to the distance between their homes
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
