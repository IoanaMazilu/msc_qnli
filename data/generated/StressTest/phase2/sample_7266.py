# Premise: Bruce and Bhishma are running on a circular track of length 600 m.
# Hypothesis: Bruce and Bhishma are running on a circular track of length more than 200 m.
# Golden Label: entailment

track_length_premise = 600
track_length_hypothesis = 200

# the hypothesis refers to the length of the track that Bruce and Bhishma are running on, which is also mentioned in the premise
if track_length_premise < track_length_hypothesis:
    # check if the actual track length in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the track length in the premise is equal to or more than the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

