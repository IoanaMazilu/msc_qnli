distance_premise = 40
distance_hypothesis = 60

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the distance in the hypothesis
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # check if the distance in the premise is less than the distance in the hypothesis
    label = "entailment"
else:
    # if the distances in the premise and the hypothesis are equal
    label = "neutral"

print(label)
