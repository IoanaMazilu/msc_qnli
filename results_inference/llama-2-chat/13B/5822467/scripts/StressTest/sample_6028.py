test_score_premise = 50
test_score_hypothesis = 50
num_tests_premise = less_than_6
num_tests_hypothesis = 4

# the hypothesis refers to the number of tests and the average test score mentioned in the premise
if test_score_hypothesis <= test_score_premise:
    # check if the estimate of 'test_score_hypothesis' contradicts the test score in the premise
    label = "contradiction"
elif num_tests_hypothesis!= num_tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
