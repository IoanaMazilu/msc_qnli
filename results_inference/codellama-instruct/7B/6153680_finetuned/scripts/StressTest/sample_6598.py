distance_apart_premise = 35
distance_apart_hypothesis = 15

# the hypothesis talks about the distance between Efrida and Frazer, which is also mentioned in the premise
if distance_apart_hypothesis >= distance_apart_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
