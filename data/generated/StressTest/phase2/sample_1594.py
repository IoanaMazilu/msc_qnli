# Premise: Jane had an average of more than 17 on his first 7 tests.
# Hypothesis: Jane had an average of 87 on his first 7 tests.
# Golden Label: neutral

average_score_premise = 17
average_score_hypothesis = 87
tests_count = 7

# the hypothesis talks about the average score of Jane's tests, referenced also in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the average score in the hypothesis contradicts the estimate of more than 'average_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

