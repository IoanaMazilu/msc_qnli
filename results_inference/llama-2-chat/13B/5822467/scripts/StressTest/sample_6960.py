test_score_premise = 60
test_score_hypothesis = 60

# the hypothesis refers to the number of tests and the average test score
if test_score_hypothesis <= test_score_premise:
    # check if the hypothesis value contradicts the estimate of the average test score in the premise
    label = "contradiction"
elif test_score_hypothesis > test_score_premise:
    # check if the hypothesis value entails the estimate of the average test score in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 2 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
