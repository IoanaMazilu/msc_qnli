# Premise: If Jack's score was within less than 4 standard deviations of the mean, what is the lowest score he could have received?
# Hypothesis: If Jack's score was within 2 standard deviations of the mean, what is the lowest score he could have received?
# Golden Label: neutral

std_deviation_premise = 4
std_deviation_hypothesis = 2

# the hypothesis talks about the number of standard deviations from the mean, which is also mentioned in the premise
if std_deviation_hypothesis >= std_deviation_premise:
    # check if the hypothesis value contradicts the premise of less than 'std_deviation_premise' standard deviations
    label = "contradiction"
else:
    # the premise gives only an upper limit for the number of standard deviations
    # any number of standard deviations less than 'std_deviation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

