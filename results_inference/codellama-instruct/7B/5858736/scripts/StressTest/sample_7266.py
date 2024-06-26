# Define variables for the numerical entities in both inputs
track_length_premise = 600
track_length_hypothesis = 200

# Extract all quantities as valid numbers
track_length_premise = int(track_length_premise)
track_length_hypothesis = int(track_length_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if track_length_hypothesis <= track_length_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'track_length_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the length of the track
    # Any length greater than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
