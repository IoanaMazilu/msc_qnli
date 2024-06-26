distance_premise = 45
distance_hypothesis = 75

# the hypothesis talks about the distance walked by Matthew, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the distance mentioned in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # the premise gives an explicit distance
    # any distance greater than 'distance_premise' is not contradicting the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
