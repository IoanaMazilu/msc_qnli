# Premise: The distance between Delhi and Mathura is less than 210 kms.
# Hypothesis: The distance between Delhi and Mathura is 110 kms.
# Golden Label: neutral

distance_premise = 210
distance_hypothesis = 110

# the hypothesis talks about the distance between Delhi and Mathura, referenced also in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

