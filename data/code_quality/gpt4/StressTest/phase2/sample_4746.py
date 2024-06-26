distance_premise = 130
distance_hypothesis = 430

# the hypothesis talks about the distance between Glen and Hannah, referenced also in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # if the hypothesis value equals the premise, we can infer entailment
    label = "entailment"
else:
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
