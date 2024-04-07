# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 78.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first 6 of 4 tests is 78.
# Golden Label: contradiction

average_score_premise = 78
num_of_tests_premise = 3

average_score_hypothesis = 78
num_of_tests_hypothesis = 6

# the hypothesis refers to the average score and number of tests mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
elif num_of_tests_hypothesis > num_of_tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

