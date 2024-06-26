distance_premise = 15
distance_hypothesis = 15

# the hypothesis talks about the distance between West-Town and East-Town, which is also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
