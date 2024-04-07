# Premise: Bruce and Bhishma are running on a circular track of length 600 m.
# Hypothesis: Bruce and Bhishma are running on a circular track of length 500 m.
# Golden Label: contradiction

track_length_premise = 600
track_length_hypothesis = 500

# the hypothesis and premise both refer to the length of the track
if track_length_hypothesis != track_length_premise:
    # check if the length of the track in the hypothesis contradicts the length given in the premise
    label = "contradiction"
else:
    # the length of the track in the hypothesis is the same as in the premise, so we can infer entailment
    label = "entailment"

print(label)

