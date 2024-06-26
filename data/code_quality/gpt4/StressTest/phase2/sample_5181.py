deviations_premise = 2
deviations_hypothesis = 1

# the hypothesis speaks about the number of standard deviations away from the mean score, which is also mentioned in the premise
if deviations_hypothesis >= deviations_premise:
    # check if the hypothesis value contradicts the premise value of 'deviations_premise'
    label = "contradiction"
elif deviations_hypothesis < deviations_premise:
    # check if the hypothesis value is less than the premise value of 'deviations_premise'
    label = "entailment"

print(label)
