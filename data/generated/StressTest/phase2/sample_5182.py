# Premise: If Jack's score was within more than 1 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: neutral

standard_deviations_premise = 1
standard_deviations_hypothesis = 2

# the hypothesis refers to the number of standard deviations from the mean for Jack's score mentioned in the premise
if standard_deviations_hypothesis < standard_deviations_premise:
    # check if the estimate of 'standard_deviations_hypothesis' contradicts the number of standard deviations in the premise
    label = "contradiction"
elif standard_deviations_hypothesis > standard_deviations_premise:
    # check if the estimate of 'standard_deviations_hypothesis' is greater than the number of standard deviations in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

