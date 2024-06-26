distance_premise = 340
distance_hypothesis = 240

# the hypothesis talks about the distance between Jack and Christina, also referenced in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise' feet
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' feet is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
