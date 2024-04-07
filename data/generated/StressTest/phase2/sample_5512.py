# Premise: The distance between Delhi and Mathura is less than 650 kms.
# Hypothesis: The distance between Delhi and Mathura is 150 kms.
# Golden Label: neutral

distance_premise = 650
distance_hypothesis = 150

# the hypothesis refers to the distance between Delhi and Mathura mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

