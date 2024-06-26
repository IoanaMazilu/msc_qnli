cities_premise = 15
cities_hypothesis = 85

# the hypothesis talks about the number of cities in a province, referenced also in the premise
if cities_hypothesis != cities_premise:
    # check if the number of cities in the hypothesis contradicts the number of cities reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
