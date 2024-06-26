score_test_premise = 83
score_test_hypothesis = 83

# the hypothesis refers to the score of the last test, which is also referenced in the premise
if score_test_hypothesis >= score_test_premise:
    # check if the hypothesis value contradicts the estimate of less than'score_test_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the score of the last test
    # any score less than'score_test_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
