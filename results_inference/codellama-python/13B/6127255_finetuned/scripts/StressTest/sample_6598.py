distance_apart_premise = 35
distance_apart_hypothesis = 15

# the hypothesis refers to the distance between Efrida and Frazer mentioned in the premise
if distance_apart_hypothesis > distance_apart_premise:
    # check if the distance in the hypothesis contradicts the estimate of 'distance_apart_premise'
    label = "contradiction"
elif distance_apart_hypothesis < distance_apart_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_apart_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis equals the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
