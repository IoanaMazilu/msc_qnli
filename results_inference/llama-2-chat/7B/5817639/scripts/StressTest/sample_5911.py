ratio_premise = 6
ratio_hypothesis = 7
sheep_needed_premise = 12880
sheep_needed_hypothesis = 12880

# the premise gives a range for the ratio, and the hypothesis gives a specific value for the ratio
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and the hypothesis gives a specific value that is consistent with the premise
    label = "entailment"

print(label)
