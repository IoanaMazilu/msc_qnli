# Premise: Bruce and Bhishma are running on a circular track of length 600 m.
# Hypothesis: Bruce and Bhishma are running on a circular track of length less than 600 m.
# Golden Label: contradiction

track_length_premise = 600
track_length_hypothesis = 600

# The hypothesis refers to the length of the circular track mentioned in the premise
if track_length_hypothesis < track_length_premise:
    # If the hypothesis suggests a track length less than the one stated in the premise, it's a contradiction
    label = "contradiction"
elif track_length_hypothesis == track_length_premise:
    # If the hypothesis suggests a track length equal to the one stated in the premise, it's an entailment
    label = "entailment"
else:
    # If the hypothesis suggests a track length greater than the one stated in the premise, it's neutral
    label = "neutral"

print(label)

