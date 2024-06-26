distance_apart_premise = 35
distance_apart_hypothesis = 15

# the hypothesis talks about the distance between Efrida and Frazer, referenced also in the premise
if distance_apart_hypothesis >= distance_apart_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_apart_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_apart_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
