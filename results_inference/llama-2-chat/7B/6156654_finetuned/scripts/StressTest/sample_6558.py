average_score_premise = 78
tests_premise = 4
tests_hypothesis = 6

# the hypothesis refers to the average score of Jerry on the first 'tests_hypothesis' tests, as mentioned in the premise
if average_score_premise >= tests_hypothesis:
    # check if the average score in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the average score in the premise is less than 'tests_hypothesis', it is consistent with the hypothesis
    # but it cannot be explicitly entailed from the hypothesis, so the label is "neutral"
    label = "neutral"

print(label)
