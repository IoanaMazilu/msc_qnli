tests_taken_premise = 3
tests_taken_hypothesis = 3 # the hypothesis suggests more than 3 tests, but we consider 3 as it's the minimum number of tests that satisfies the condition
average_score_premise = 85
average_score_hypothesis = 85

# the hypothesis talks about the number of tests taken and the average score, which are also referenced in the premise
if tests_taken_hypothesis <= tests_taken_premise and average_score_hypothesis != average_score_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif tests_taken_hypothesis > tests_taken_premise and average_score_hypothesis == average_score_premise:
    # if the number of tests taken in the hypothesis is greater than the premise and the average score remains the same
    # we can't explicitly infer that from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
