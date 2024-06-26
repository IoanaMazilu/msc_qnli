distance_premise = 45
distance_hypothesis = 85

# The hypothesis talks about the same event mentioned in the premise,
# but gives a different estimate for the distance Matthew walked
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance given in the premise
    label = "contradiction"
else:
    # if the distances in the premise and the hypothesis match, we can infer entailment
    label = "entailment"

print(label)
