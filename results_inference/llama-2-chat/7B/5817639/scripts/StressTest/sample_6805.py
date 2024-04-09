distance_premise = 81
distance_hypothesis = 31

# the hypothesis talks about the distance traveled by Bob, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Bob
    # any distance traveled by Bob less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
