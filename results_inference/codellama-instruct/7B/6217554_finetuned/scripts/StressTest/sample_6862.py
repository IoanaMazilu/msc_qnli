distance_km_premise = 35
distance_km_hypothesis = 45

# the hypothesis talks about the distance traveled by Johnny, referenced also in the premise
if distance_km_hypothesis <= distance_km_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_km_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Johnny
    # any distance greater than 'distance_km_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
