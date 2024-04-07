# Premise: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within less than 4 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: entailment

std_deviation_premise = 2
std_deviation_hypothesis = 4

# the hypothesis refers to the number of standard deviations of Jack's score mentioned in the premise
if std_deviation_premise > std_deviation_hypothesis:
    # check if the 'std_deviation_hypothesis' contradicts the number of standard deviations in the premise
    label = "contradiction"
elif std_deviation_premise < std_deviation_hypothesis:
    # check if the number of standard deviations in the hypothesis contradicts the number of standard deviations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

