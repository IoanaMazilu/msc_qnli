distance_premise = 35
distance_hypothesis = 45

# the hypothesis talks about the distance Matthew walked, referenced also in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and premise value are equal, we can infer entailment
    label = "entailment"

print(label)
