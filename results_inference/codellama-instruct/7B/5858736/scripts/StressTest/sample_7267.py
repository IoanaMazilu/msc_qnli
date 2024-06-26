# Define variables for the numerical entities in the premise and hypothesis
track_length_premise = 200
track_length_hypothesis = 600

# Check if the hypothesis value contradicts the estimate of more than 'track_length_premise'
if track_length_hypothesis <= track_length_premise:
    label = "contradiction"
else:
    # Any number of meters greater than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
