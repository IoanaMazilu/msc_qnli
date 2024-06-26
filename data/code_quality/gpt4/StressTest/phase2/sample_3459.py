std_dev_premise = 2
std_dev_hypothesis = 6

# the hypothesis refers to the number of standard deviations from the mean score mentioned in the premise
if std_dev_premise > std_dev_hypothesis:
    # check if the number of 'std_dev_hypothesis' contradicts the number of standard deviations in the premise
    label = "contradiction"
elif std_dev_premise == std_dev_hypothesis:
    # check if the number of standard deviations in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones but can't be fully entailed, we can infer neutral relation
    label = "neutral"

print(label)
