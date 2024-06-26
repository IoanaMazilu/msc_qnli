test_scores_premise = [78, 80, 82]
test_scores_hypothesis = [78, 80, 82, 85]

# the hypothesis refers to the number of tests mentioned in the premise
if len(test_scores_hypothesis) <= len(test_scores_premise):
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'len(test_scores_premise)' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
