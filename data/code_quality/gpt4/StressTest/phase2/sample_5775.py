distance_apart_premise = 240
distance_apart_hypothesis = 340

# the hypothesis talks about the distance between Jack and Christina, mentioned also in the premise
if distance_apart_hypothesis < distance_apart_premise:
    # check if the hypothesis value contradicts the value given in the premise
    label = "contradiction"
elif distance_apart_hypothesis == distance_apart_premise:
    # the distance in the hypothesis is exactly the same as in the premise
    label = "entailment"
else:
    # the premise gives an exact distance, any distance more than 'distance_apart_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
