distance_walked_premise = 17
distance_walked_hypothesis = 27

# the hypothesis talks about the distance walked from X to Y, which is also referenced in the premise
if distance_walked_hypothesis != distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the distance walked mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
