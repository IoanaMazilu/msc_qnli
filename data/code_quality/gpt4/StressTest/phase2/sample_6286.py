total_tests_premise = 10
average_score_premise = 83
test_number_premise = 70

total_tests_hypothesis = 10
average_score_hypothesis = 83
test_number_hypothesis = 10

# the premise and hypothesis refer to the number of tests, the average score, and the number of the test Robin must score
if total_tests_premise != total_tests_hypothesis:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
elif average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif test_number_hypothesis >= test_number_premise:
    # check if the number of the test in the hypothesis contradicts the estimate of less than 'test_number_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of the test
    # any test number less than 'test_number_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
