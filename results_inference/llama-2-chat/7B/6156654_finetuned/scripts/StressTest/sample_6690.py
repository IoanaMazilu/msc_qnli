distance_rakesh_premise = 1800
distance_rakesh_hypothesis = 8800

# the hypothesis refers to the distance Rakesh travelled by air, which is also mentioned in the premise
if distance_rakesh_hypothesis <= distance_rakesh_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif distance_rakesh_hypothesis > distance_rakesh_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it is neutral
    label = "neutral"

print(label)
