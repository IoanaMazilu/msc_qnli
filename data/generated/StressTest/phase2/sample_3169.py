# Premise: Arjun and Bhishma are running on a circular track of length less than 800 m.
# Hypothesis: Arjun and Bhishma are running on a circular track of length 600 m.
# Golden Label: neutral

track_length_premise = 800
track_length_hypothesis = 600

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_hypothesis >= track_length_premise:
    # check if the length of the track in the hypothesis contradicts the estimate of less than 'track_length_premise'
    label = "contradiction"
elif track_length_hypothesis < track_length_premise:
    # the premise gives only an estimate for the length of the track
    # any length of track less than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

