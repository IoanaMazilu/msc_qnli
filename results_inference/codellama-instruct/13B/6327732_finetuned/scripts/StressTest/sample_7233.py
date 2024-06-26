sisters_distance_premise = 2
sisters_distance_hypothesis = 3

# the hypothesis refers to the distance run by the twin sisters, mentioned in the premise
if sisters_distance_hypothesis >= sisters_distance_premise:
    # check if the estimate of'sisters_distance_hypothesis' contradicts the distance run by the twin sisters in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance run by the twin sisters
    # any distance less than'sisters_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
