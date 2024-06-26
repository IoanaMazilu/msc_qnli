distance_apart_premise = 10
distance_apart_hypothesis = 10

# the hypothesis talks about the distance between Efrida and Frazer, mentioned also in the premise
if distance_apart_hypothesis != distance_apart_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
