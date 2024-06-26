distance_apart_premise = 62
distance_apart_hypothesis = 12

# the hypothesis refers to the distance between Efrida's and Frazer's homes mentioned in the premise
if distance_apart_hypothesis > distance_apart_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif distance_apart_hypothesis < distance_apart_premise:
    # the premise gives a maximum distance for the homes
    # any distance less than 'distance_apart_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
