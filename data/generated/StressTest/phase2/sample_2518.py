# Premise: The distance between Delhi and Mathura is less than 530 kms.
# Hypothesis: The distance between Delhi and Mathura is 130 kms.
# Golden Label: neutral

distance_premise = 530
distance_hypothesis = 130

# the hypothesis talks about the distance between two cities, also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

