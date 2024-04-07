# Premise: If Jack's score was within less than 7 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: neutral

deviations_premise = 7
deviations_hypothesis = 2

# both the hypothesis and the premise refer to the number of standard deviations that Jack's score could be from the mean
if deviations_hypothesis > deviations_premise:
    # check if the number of 'deviations_hypothesis' contradicts the number of 'deviations_premise'
    label = "contradiction"
elif deviations_hypothesis == deviations_premise:
    # if both are equal, that is an entailment
    label = "entailment"
else:
    # if the 'deviations_hypothesis' is less than 'deviations_premise', it doesn't contradict but also not explicitly entailed
    label = "neutral"

print(label)

