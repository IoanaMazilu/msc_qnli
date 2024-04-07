# Premise: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within more than 2 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: contradiction

standard_deviations_premise = 2
standard_deviations_hypothesis = 2

# the hypothesis refers to the number of standard deviations from the mean of Jack's score, which is also mentioned in the premise
if standard_deviations_hypothesis != standard_deviations_premise:
    # check if the number of standard deviations in the hypothesis contradicts the number of standard deviations in the premise
    label = "contradiction"
else:
    # if the number of standard deviations in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

