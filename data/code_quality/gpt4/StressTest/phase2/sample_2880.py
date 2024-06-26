tests_taken_premise = 3
tests_taken_hypothesis = 7
test_score_premise = 94
test_score_hypothesis = 94

# the hypothesis talks about the average score of Jerry on his first few tests, which is also mentioned in the premise
if tests_taken_hypothesis > tests_taken_premise:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken in the premise
    label = "contradiction"
elif test_score_hypothesis != test_score_premise:
    # check if the test score in the hypothesis contradicts the test score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
