distance_premise = 20
speed_maxwell_premise = 4
speed_brad_premise = 6
distance_hypothesis = 80

# the hypothesis refers to the same situation as the premise
# but with a different distance
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value,
    # we can infer entailment
    label = "entailment"

print(label)
