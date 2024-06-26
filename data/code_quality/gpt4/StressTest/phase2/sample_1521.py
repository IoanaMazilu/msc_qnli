distance_premise = 40
distance_hypothesis = 50

# the hypothesis refers to the distance between Marathon and Athens, also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the explicit distance of 'distance_premise'
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # any distance less than 'distance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesized distance is exactly the same as the one in the premise, we can infer entailment
    label = "entailment"

print(label)
