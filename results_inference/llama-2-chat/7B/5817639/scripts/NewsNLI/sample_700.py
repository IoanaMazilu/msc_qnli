locations_premise = 70
locations_hypothesis = 70
colombians_premise = 200
colombians_hypothesis = 200

# the hypothesis mentions the same number of locations and the same number of rescued people as the premise
if locations_hypothesis == locations_premise and colombians_hypothesis == colombians_premise:
    # if the values in the hypothesis match the values in the premise, we can infer entailment
    label = "entailment"
else:
    # if the values in the hypothesis contradict the values in the premise, we can infer contradiction
    label = "contradiction"

print(label)
