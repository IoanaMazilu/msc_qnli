apartment_distance_premise = 35
apartment_distance_hypothesis = 15

# the hypothesis talks about the distance between Efrida and Frazer's apartments, referenced also in the premise
if apartment_distance_hypothesis >= apartment_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apartment_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Efrida and Frazer's apartments
    # any distance less than 'apartment_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
