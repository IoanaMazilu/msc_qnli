# define variables for the numerical entities in the premise and hypothesis
joe_test_scores_premise = 60
num_tests_premise = 4

# define variables for the numerical entities in the hypothesis
joe_test_scores_hypothesis = 60
num_tests_hypothesis = float(more_than_4)

# check if the hypothesis value contradicts the premise value
if joe_test_scores_hypothesis!= joe_test_scores_premise:
    # check if the hypothesis value contradicts the estimate of more than 4 tests
    if num_tests_hypothesis <= num_tests_premise:
        label = "contradiction"
    else:
        label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
