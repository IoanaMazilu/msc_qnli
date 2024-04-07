# Premise: Bruce and Bhishma are running on a circular track of length more than 200 m.
# Hypothesis: Bruce and Bhishma are running on a circular track of length 600 m.
# Golden Label: neutral

track_length_premise = 200
track_length_hypothesis = 600

# the hypothesis refers to the length of the circular track mentioned in the premise
if track_length_hypothesis <= track_length_premise:
    # check if the hypothesized track length contradicts the estimate of more than 'track_length_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the track length
    # any track length greater than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

