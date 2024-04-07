# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 40.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 4 equally weighted tests was 40.
# Golden Label: contradiction

test_score_premise = 40
number_of_tests_premise = 4
test_score_hypothesis = 40
number_of_tests_hypothesis = 4

# the hypothesis refers to Joe's average test score and the number of tests, both mentioned in the premise
if test_score_hypothesis != test_score_premise:
    # check if the test score in the hypothesis contradicts the test score in the premise
    label = "contradiction"
elif number_of_tests_hypothesis >= number_of_tests_premise:
    # check if the number of tests in the hypothesis contradicts the premise where tests are less than 'number_of_tests_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

