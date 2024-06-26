distance_travelled_premise = 250
distance_travelled_hypothesis = 250

# The hypothesis is about the distance that Louisa travelled, which is also mentioned in the premise.
if distance_travelled_hypothesis >= distance_travelled_premise:
    # Check if the hypothesis distance contradicts the premise distance.
    label = "contradiction"
else:
    # The premise and hypothesis mention the exact same distance, so if the hypothesis distance is not greater,
    # we can infer entailment.
    label = "entailment"

print(label)
