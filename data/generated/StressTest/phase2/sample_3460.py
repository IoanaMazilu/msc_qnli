# Premise: If Jack's score was within less than 6 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: neutral

std_dev_premise = 6
std_dev_hypothesis = 2

# the hypothesis refers to the number of standard deviations from the mean of Jack's score, mentioned in the premise
if std_dev_hypothesis >= std_dev_premise:
    # check if the number of standard deviations in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif std_dev_hypothesis < std_dev_premise:
    # if the number of standard deviations in the hypothesis is less than in the premise
    # we can infer entailment, because being within 2 standard deviations is a subset of being within 6 standard deviations
    label = "entailment"

print(label)

