distance_premise = 35
distance_hypothesis = 15

# the hypothesis refers to the distance between Efrida and Frazer, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Efrida and Frazer
    # any distance between Efrida and Frazer that is less than or equal to 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
