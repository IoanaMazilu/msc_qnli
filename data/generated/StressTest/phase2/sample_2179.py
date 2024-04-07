# Premise: If Jack's score was within less than 3 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: neutral

std_deviation_premise = 3
std_deviation_hypothesis = 2

# the hypothesis refers to the number of standard deviations of Jack's score mentioned in the premise
if std_deviation_hypothesis >= std_deviation_premise:
    # check if the number of standard deviations in the hypothesis contradicts the number of standard deviations mentioned in the premise
    label = "contradiction"
elif std_deviation_hypothesis < std_deviation_premise:
    # check if the number of standard deviations in the hypothesis is within the limit mentioned in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

