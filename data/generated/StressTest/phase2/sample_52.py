# Premise: Bruce and Bhishma are running on a circular track of length less than 800 m.
# Hypothesis: Bruce and Bhishma are running on a circular track of length 600 m.
# Golden Label: neutral

track_length_premise = 800
track_length_hypothesis = 600

# Hypothesis and premise both make claims about the length of the circular track
if track_length_hypothesis >= track_length_premise:
    # Check if the length of the track in the hypothesis contradicts the premise's maximum length
    label = 'contradiction'
else:
    # The premise only estimates that the track is less than 800m
    # Any track length less than 800m is consistent with the premise, but cannot be explicitly entailed from it
    label = 'neutral'

print(label)

