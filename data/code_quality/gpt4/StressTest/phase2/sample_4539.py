std_dev_premise = 2
std_dev_hypothesis = 7

# Both premise and hypothesis talk about the number of standard deviations from the mean for Jack's score
if std_dev_hypothesis < std_dev_premise:
    # check if the number of standard deviations in the hypothesis contradicts the number of standard deviations in the premise
    label = "contradiction"
elif std_dev_hypothesis == std_dev_premise:
    # if the number of standard deviations in the hypothesis and premise are equal, it is an entailment
    label = "entailment"
else:
    # if the number of standard deviations in the hypothesis is greater than in the premise, it is neutral
    label = "neutral"

print(label)
