# Premise: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within 8 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: contradiction

deviations_premise = 2
deviations_hypothesis = 8

# the hypothesis refers to the number of standard deviations from the mean score mentioned in the premise
if deviations_hypothesis < deviations_premise:
    # check if the number of 'deviations_hypothesis' contradicts the number of standard deviations in the premise
    label = "contradiction"
elif deviations_hypothesis > deviations_premise:
    # the premise gives only an estimate for the number of standard deviations
    # any number of standard deviations greater than 'deviations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

