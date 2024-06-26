distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance between X and Y, also mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the premise distance contradicts the estimate of less than 'distance_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # the hypothesis gives a higher estimate for the distance
    # any distance less than 'distance_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)