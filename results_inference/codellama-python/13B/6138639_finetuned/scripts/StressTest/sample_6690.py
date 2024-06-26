distance_travelled_premise = 1800
distance_travelled_hypothesis = 8800

if distance_travelled_hypothesis <= distance_travelled_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_travelled_premise'
    label = "contradiction"
else:
    # the premise gives an exact distance travelled
    # any distance greater than 'distance_travelled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
