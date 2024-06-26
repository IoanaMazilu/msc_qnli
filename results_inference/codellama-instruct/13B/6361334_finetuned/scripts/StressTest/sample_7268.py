circular_track_premise = 600
circular_track_hypothesis = 500

# the hypothesis refers to the length of the circular track mentioned in the premise
if circular_track_hypothesis >= circular_track_premise:
    # check if the hypothesis value contradicts the length of the circular track in the premise
    label = "contradiction"
else:
    # the premise gives an exact length for the circular track
    # any length less than 'circular_track_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
